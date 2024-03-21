import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"
site = requests.get(url)


sitehtml = BeautifulSoup(site.text.lower(), features="html.parser")
idk = sitehtml.prettify()

test = sitehtml.find_all("div", class_="col-md-4 country")

while True:
    country = input("What country would you like to find the population of?: ").lower()
    if country == "done": #gives up
        break
    if country == "usa" or country == "united states of america" or country == "us": #USA NUMBER 1 RAHHHHHH
        country = "united states"
    
    #Just like loops thru the different country class div's frfr no cap
    for div in test:
        countryclass = div.find("h3", class_="country-name")
        
        #Kinda just does some silly stuff
        if country == countryclass.text.strip():
            countrypop = div.find("span", class_="country-population")
            print("The population of " + country + " is: " + countrypop.text.strip())