from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

# Part 1 - Scrape the links, addresses, and prices of the rental properties

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
rentals_page = response.text
soup = BeautifulSoup(rentals_page, "html.parser")
# print(soup)
apartment_all_links = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
all_links = [link["href"] for link in apartment_all_links]
print(all_links)

apartment_all_addreses = soup.find_all(name="address")
all_addreses = [address.getText().replace(" | ", " ").strip() for address in apartment_all_addreses]
print(all_addreses)

apartment_all_prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
all_prices = [price.getText().replace("/mo", "").strip("+") for price in apartment_all_prices]
print(all_prices)

# Part 2 - Fill in the Google Form using Selenium

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc1_Cj56J4dBIL-7CpFBPda8wmWPfpX0eKABJC3FL6DoBcA2w/viewform")
    time.sleep(3)

    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(all_links[n])

    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    address.send_keys(all_addreses[n])

    prices = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    prices.send_keys(all_prices[n])

    button = driver.find_element(By.CLASS_NAME, "l4V7wb.Fxmcue")
    button.click()






