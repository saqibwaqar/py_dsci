from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdx4EDE23VHj3FaJgh9zFiUfDwA79GteL_tZnrOD0-VBQXidQ/viewform?usp=sf_link"

response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")

soup = BeautifulSoup(response.text, "html.parser")

price_list = [span.get_text().replace("/mo", "").split("+")[0]
              for span in soup.select(selector=".PropertyCardWrapper__StyledPriceLine")]

weblinks = [anchor["href"] for anchor in
            soup.select(selector=".StyledPropertyCardDataWrapper a")]

address_list = [address.get_text().strip().replace("|", "") for address in
                soup.select(selector=".ListItem-c11n-8-84-3-StyledListCardWrapper a address")]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
chrome_options.add_argument("--start-maximized")

webdriver = webdriver.Chrome(options=chrome_options)
webdriver.get(GOOGLE_FORM)

sleep(3)

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
        weblinks[index]).perform()

    # Click submit button
    submit = webdriver.find_element(By.CSS_SELECTOR, value=".NPEfkd.RveJvd.snByac")
    submit.click()

    # Submit another response
    submit_another = webdriver.find_element(By.CSS_SELECTOR, value=".c2gzEf a")
    submit_another.click()
