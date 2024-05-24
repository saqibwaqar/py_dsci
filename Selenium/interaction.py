from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=False)
chrome_options.add_argument("--start-maximized")

webdriver = webdriver.Chrome(options=chrome_options)
webdriver.get("https://en.wikipedia.org/wiki/Main_Page")

# count = webdriver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]').text
article_count = webdriver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)

webdriver.quit()
