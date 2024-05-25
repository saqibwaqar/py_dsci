import time
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

webdriver = webdriver.Chrome(options=chrome_options)
webdriver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = webdriver.find_element(By.ID, value="cookie")

is_game_on = True
start = time.time()


# def find_upgrades_menu(driver):
#     upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store div")
#     return {upgrade.get_attribute("id"): upgrade.find_element(By.CSS_SELECTOR, value="b").text.split("-")[1].strip()
#             for upgrade in upgrades if upgrade.find_element(By.CSS_SELECTOR, value="b").text != ""}

def find_upgrades_menu(driver):
    upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    return {
        int(upgrade.find_element(By.CSS_SELECTOR, value="b").text.split("-")[1].strip().replace(",",
                                                                                                "")): upgrade.get_attribute(
            "id")
        for upgrade in upgrades if upgrade.find_element(By.CSS_SELECTOR, value="b").text != ""}


def get_money(driver):
    return int(driver.find_element(By.ID, value="money").text.replace(",",
                                                                      ""))


upgrades_dict = find_upgrades_menu(webdriver)
pprint(upgrades_dict)
my_keys = list(upgrades_dict.keys())
my_keys.sort(reverse=True)

while is_game_on:
    cookie.click()
    end = time.time()
    elapsed_time = round(end - start)

    if elapsed_time % 10 == 0:
        # start = time.time()
        print(f"{elapsed_time} seconds elapsed")

        # Check for the  most expensive affordable upgrade in upgrade_dict
        money = get_money(webdriver)
        for key in my_keys:
            if money >= key:
                expensive_item = webdriver.find_element(By.ID, value=upgrades_dict[key])
                expensive_item.click()
                # break
                money = get_money(webdriver)

    if elapsed_time == 300:  # 300 seconds for 5 minutes
        is_game_on = False
        cps = webdriver.find_element(By.ID, value="cps")
        print(f"{cps.text}")
