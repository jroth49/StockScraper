from bs4 import BeautifulSoup
import requests

#websites html and soup obj
website = requests.get("https://money.cnn.com/data/hotstocks/");
soup = BeautifulSoup(website.text, features="html.parser");

#preScrape
indexStock = 12;
print("ABRV - Price - $Change - %Change");

#Scrapes GainersList
while (indexStock < 21):
    stockLet = soup.find_all("tr")[indexStock].find("a").get_text()
    stockPrice = soup.find_all("tr")[indexStock].find_all("span")[1].get_text()
    stockChan = soup.find_all("tr")[indexStock].find_all("span")[2].get_text()
    stockPerc = soup.find_all("tr")[indexStock].find_all("span")[4].get_text()
    print(stockLet + " - " + stockPrice + " - " + stockChan + " - " + stockPerc);
    indexStock = indexStock + 1; 






