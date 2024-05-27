from pprint import pprint
from time import sleep

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdx4EDE23VHj3FaJgh9zFiUfDwA79GteL_tZnrOD0-VBQXidQ/viewform?usp=sf_link"

response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")

soup = BeautifulSoup(response.text, "html.parser")

li_list = soup.select(selector=".List-c11n-8-84-3-photo-cards li")
anchor_tags = soup.select(selector=".List-c11n-8-84-3-photo-cards li .StyledPropertyCardDataArea-anchor")

print(li_list)

price_list = [li.find(name="span", class_="PropertyCardWrapper__StyledPriceLine").get_text().split("+")[0].split("/")[0]
              for li in
              li_list if li.find(name="span", class_="PropertyCardWrapper__StyledPriceLine") is not None]
print(price_list)
print(len(price_list))

href_list = [anchor.get("href") for anchor in anchor_tags]

print(href_list)
print(len(href_list))

address_list = [anchor.find(name="address").get_text().strip().replace("|", "") for anchor in anchor_tags]
print(address_list)
print(len(address_list))

#############part 1 done###################

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
chrome_options.add_argument("--start-maximized")

webdriver = webdriver.Chrome(options=chrome_options)
webdriver.get(GOOGLE_FORM)

for index in range(len(price_list)):
    address_input = webdriver.find_element(By.XPATH,
                                           value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")

    price_input = webdriver.find_element(By.XPATH,
                                         value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")

    href_input = webdriver.find_element(By.XPATH,
                                        value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")

    webdriver.implicitly_wait(10)

    ActionChains(webdriver).move_to_element(address_input).send_keys_to_element(address_input,
                                                                                address_list[index]).move_to_element(
        price_input).send_keys_to_element(price_input, price_list[index]).move_to_element(
        href_input).send_keys_to_element(
        href_input,
        href_list[index]).perform()

    # click submit button
    submit = webdriver.find_element(By.CSS_SELECTOR, value=".NPEfkd.RveJvd.snByac")
    submit.click()

    # Submit another response
    submit_another = webdriver.find_element(By.CSS_SELECTOR, value=".c2gzEf a")
    submit_another.click()
