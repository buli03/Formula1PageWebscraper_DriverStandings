from selenium import webdriver 
import datetime
from bs4 import BeautifulSoup as bs

#variables
today = datetime.date.today();
year = today.year
doContinue = True

#functions
def get_Text(e):
    if e is None:
        return ""
    return e.text

#program
while doContinue == True: 
    print("\n>>> Do you wish to continue? y/n")
    doContinueInput = input()
    if (doContinueInput.lower() == "n" or doContinueInput.lower() == "no"):
        doContinueInput = False
        break
    print("\n>>> Which year do you want to check? ")
    print(f">>> ( Pick from 1958 to {year} )")

    pickedyear = int(input())

    if (pickedyear >= 1958 and pickedyear <= year):
        y = webdriver.Chrome()
        y.get(f"https://www.formula1.com/en/results.html/{pickedyear}/drivers.html")
        standings2 = y.page_source
        y.get(f"https://www.formula1.com/en/results.html/{pickedyear}/team.html")
        teamStandings = y.page_source
        y.quit()

        standingsS = bs(standings2, 'html.parser')
        standingsSS = standingsS.find_all("tr")

        print(f"\n----------------------------{pickedyear} Driver Standings--------------------------------")
        for driver in standingsSS[1:]:
            print(get_Text(driver.find("td",class_="dark")),":",
                get_Text(driver.find("span",class_="hide-for-tablet")),
                get_Text(driver.find("span",class_="hide-for-mobile")), "|", 
                get_Text(driver.find("a",class_="grey semi-bold uppercase ArchiveLink")), "=>",
                get_Text(driver.find("td",class_="dark bold")), "pts")

        print(f"\n-----------------------------{pickedyear} Team Standings---------------------------------")

        teamStandingsS = bs(teamStandings, "html.parser")
        teamStandingsSS = teamStandingsS.find_all("tr")
        for team in teamStandingsSS[1:]:
            print(get_Text(team.find("td",class_="dark")),":",
                get_Text(team.find("a",class_="dark bold uppercase ArchiveLink")),"=>",
                get_Text(team.find("td",class_="dark bold")), "pts")
    else: 
        print(">>> WRONG DATE")
