from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import os

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

webdriver = webdriver.Chrome(options=chrome_options)
webdriver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3932146189&f_AL=true&f_I=4%2C6%2C8%2C1594%2C118&f_PP=100205264%2C103289019%2C104524176%2C100170895%2C100264288&f_T=9%2C39%2C10738%2C23347%2C30128&geoId=91000008&keywords=software%20engineer&location=MENA&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R&spellCorrectionEnabled=true")

sign_in = webdriver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()

sleep(3)

email_input = webdriver.find_element(By.ID, value="username")
email_input.send_keys(EMAIL)

password_input = webdriver.find_element(By.ID, value="password")
password_input.send_keys(PASSWORD)

sign_in_button = webdriver.find_element(By.CSS_SELECTOR, value=".btn__primary--large.from__button--floating")
sign_in_button.click()

sleep(35)

# Select a job
easy_apply = webdriver.find_element(By.CSS_SELECTOR,
                                    value='.jobs-apply-button.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view')
easy_apply.click()

sleep(2)

mobile_number = webdriver.find_element(By.CSS_SELECTOR, value=".artdeco-text-input--input")
mobile_number.send_keys("")

next_button = webdriver.find_element(By.CSS_SELECTOR,
                                     value=".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
next_button.click()
next_button.click()

sleep(2)
yes_radio = webdriver.find_element(By.CSS_SELECTOR,
                                   value='label[for="urn:li:fsd_formElement:urn:li:jobs_applyformcommon_easyApplyFormElement:(3932146189,295032257,multipleChoice)-0"]')
yes_radio.click()

experience_input = webdriver.find_element(By.CSS_SELECTOR, value='.artdeco-text-input--input')
experience_input.send_keys("0")

review_button = webdriver.find_element(By.CSS_SELECTOR,
                                       value='.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
review_button.click()

submit_button = webdriver.find_element(By.CSS_SELECTOR,
                                       value=".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
submit_button.click()
