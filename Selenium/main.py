from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By

# Remain open browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

webdriver = webdriver.Chrome(options=chrome_options)
# webdriver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
#
# price_whole = webdriver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = webdriver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(price_whole.text)
# print(price_cents.tag_name)
# print(f"The price is ${price_whole.text} and {price_cents.text} cents")

webdriver.get("https://www.python.org/")

# search_bar = webdriver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# print(search_bar.tag_name)

# go_button = webdriver.find_element(By.ID, value="submit")
# print(go_button.size)
# link = webdriver.find_element(By.CSS_SELECTOR, value=".tier-1.element-4 a")
# print(link.text)

# Xpath
# link = webdriver.find_element(By.XPATH, value='//*[@id="container"]/li[3]/ul/li[3]')
# print(link.text)
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/time

# #Way1
# list_items = webdriver.find_elements(By.CSS_SELECTOR, value='.medium-widget.event-widget.last li')
# print(len(list_items))
#
# date_events = {list_items.index(li): {
#     'time': li.find_element(By.CSS_SELECTOR, value="time").get_attribute("datetime").split("T")[0],
#     'name': li.find_element(By.CSS_SELECTOR, value="a").text} for li in list_items}

# Way2

time_list = webdriver.find_elements(By.CSS_SELECTOR, value=".medium-widget.event-widget.last li time")
event_list = webdriver.find_elements(By.CSS_SELECTOR, value=".medium-widget.event-widget.last li a")
date_events = {}
for n in range(len(time_list)):
    date_events[n] = {
        'time': time_list[n].text,
        'name': event_list[n].text
    }

pprint(date_events)
# webdriver.maximize_window()
# webdriver.close()
webdriver.quit()
