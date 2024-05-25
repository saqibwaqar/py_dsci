import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

webdriver = webdriver.Chrome(options=chrome_options)
webdriver.get("https://orteil.dashnet.org/experiments/cookie/")


def get_upgrades_menu():
    upgrades = webdriver.find_elements(By.CSS_SELECTOR, value="#store div")
    return {
        int(item.find_element(By.CSS_SELECTOR, value="b").text.split("-")[1].strip().replace(",", "")):
            item.get_attribute("id") for item in upgrades if item.find_element(By.CSS_SELECTOR, value="b").text != ""
    }


def get_money():
    return int(webdriver.find_element(By.ID, value="money").text.replace(",", ""))


upgrades_dict = get_upgrades_menu()
keys = list(upgrades_dict.keys())

cookie = webdriver.find_element(By.ID, value="cookie")

timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5 minutes
is_game_on = True

while is_game_on:
    cookie.click()
    if time.time() > timeout:
        # Check for the  most expensive affordable upgrade in upgrade_dict
        money = get_money()
        expensive_item_keys = [key for key in keys if money >= key]
        most_expensive_item_key = max(expensive_item_keys)
        expensive_item = webdriver.find_element(By.ID, value=upgrades_dict[most_expensive_item_key])
        expensive_item.click()

        timeout = time.time() + 5

    if time.time() > five_min:  # 300 seconds for 5 minutes
        is_game_on = False
        cps = webdriver.find_element(By.ID, value="cps")
        print(f"{cps.text}")
