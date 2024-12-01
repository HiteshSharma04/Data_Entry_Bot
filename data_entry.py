from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ADD1  ="https://docs.google.com/forms/d/e/1FAIpQLScABG7gFgSTJxZaeGaBaiV-eYoGJCnyAXagu0xB9iL7ZPI8Qw/viewform?usp=sf_link"
ADD2 = "https://appbrewery.github.io/Zillow-Clone/"

para = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
}
response = requests.get(url=ADD2, headers=para)
data = response.text
soup = BeautifulSoup(data, "html.parser")

tag_link = soup.select(".StyledPropertyCardDataWrapper a")
tag_address = soup.select(".StyledPropertyCardDataWrapper address")
tag_price = soup.select(".StyledPropertyCardDataWrapper span")
# print(tags)
links = []
prices = []
addresses = []

for tag in tag_link:
    tag1 = tag["href"]
    links.append(tag1)
print(links)

for tag in tag_address:
    tag1 = tag.text.strip().replace("\n", "").replace("|", "")
    addresses.append(tag1)
print(addresses)

for tag in tag_price:
    tag1 = tag.text.replace("/mo", "").split("+")[0]
    prices.append(tag1)
print(prices)

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

driver.get(ADD1)
time.sleep(2)
try:
    for i in range(len(addresses)):
        addres = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        addres.send_keys(addresses[i])

        cost = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        cost.send_keys(prices[i])

        go = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        go.send_keys(links[i])

        tap = driver.find_element(By.CLASS_NAME, "l4V7wb")
        tap.click()
        time.sleep(2)
        another = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        another.click()
except Exception as e:
    print("failed", e)
