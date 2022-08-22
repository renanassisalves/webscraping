import time

import requests
from classes import Team
from bs4 import BeautifulSoup

s = requests.session()


def doRequest(page_number):
    __url = f"https://www.scrapethissite.com/pages/forms/?page_num={page_number}"
    __request = s.get(__url)
    if __request.status_code == 200:
        return BeautifulSoup(__request.text, 'html.parser')
    else:
        raise Exception("Could not get site data properly")


def scrapTeams(data):
    __teams = []

    for team in data.find_all("tr", attrs={"class": "team"}):
        name = team.findNext("td", attrs={"class": "name"}).text.replace("\n", "").strip()
        year = team.findNext("td", attrs={"class": "year"}).text.replace("\n", "").strip()
        wins = team.findNext("td", attrs={"class": "year"}).text.replace("\n", "").strip()
        losses = team.findNext("td", attrs={"class": "year"}).text.replace("\n", "").strip()
        otLosses = team.findNext("td", attrs={"class": "ot-losses"}).text.replace("\n", "").strip()
        winPercentage = team.findNext("td", attrs={"class": "pct"}).text.replace("\n", "").strip()
        goalsFor = team.findNext("td", attrs={"class": "gf"}).text.replace("\n", "").strip()
        goalsAgainst = team.findNext("td", attrs={"class": "ga"}).text.replace("\n", "").strip()
        plusMinus = team.findNext("td", attrs={"class": "diff"}).text.replace("\n", "").strip()

        team = Team(name, year, wins, losses, otLosses,
                    winPercentage, goalsFor, goalsAgainst, plusMinus)
        __teams.append(team)

    return __teams


def checkHasNext(data):
    if data.find_all("a", attrs={"aria-label": "Next"}):
        return True
    else:
        return False


def main():
    i = 1
    teams = []
    hasNext = True
    while hasNext:
        print(f"Scrapping page: {i}")
        data = doRequest(i)
        hasNext = checkHasNext(data)
        teams.extend(scrapTeams(data))
        i = i + 1

    print(f"\n\nGot data from {len(teams)} teams.")
    print("Printing them in 5 seconds...\n\n")
    time.sleep(5)
    for team in teams:
        print(team.__str__())
        time.sleep(0.2)
    print(f"Finished printing all teams data ")


if __name__ == "__main__":
    main()
