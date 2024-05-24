from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
chrome_options.add_argument("--start-maximized")

webdriver = webdriver.Chrome(options=chrome_options)
# webdriver.get("https://en.wikipedia.org/wiki/Main_Page")
webdriver.get("https://secure-retreat-92358.herokuapp.com/")

# count = webdriver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]').text
# article_count = webdriver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)

# Clicking using tag
# article_count.click()

# Click using Link Text
# a_tag = webdriver.find_element(By.LINK_TEXT, value="Sim0ne")
# print(a_tag.tag_name)
# a_tag.click()

# Input in form
# input_tag = webdriver.find_element(By.NAME, value="search")
# input_tag.send_keys("Python")

# Hit Enter
# input_tag = webdriver.find_element(By.NAME, value="search")
# input_tag.send_keys("Python", Keys.ENTER)

# Input Form App Brewery
fName = webdriver.find_element(By.NAME, value="fName")
lName = webdriver.find_element(By.NAME, value="lName")
email = webdriver.find_element(By.NAME, value="email")

fName.send_keys("Swam")
lName.send_keys("Maws")
email.send_keys("abc@cda.com")

button = webdriver.find_element(By.CSS_SELECTOR, value=".btn-primary")
button.click()
# webdriver.quit()
