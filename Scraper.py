import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"
site = requests.get(url)

sitehtml = BeautifulSoup(site.text.lower(), features="html.parser")
idk = sitehtml.prettify()

#test = sitehtml.find_all("span", {"class": "country-population"})
test = sitehtml.find_all('h3 class="country-name"')
print(test)