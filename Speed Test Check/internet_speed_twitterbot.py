from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

SPEED_TEST_URL = "https://www.speedtest.net/"
X_URL = "https://x.com/login"

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")


class InternetSpeedTwitterBot:

    def __init__(self):
        self.up = 0
        self.down = 0
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option(name="detach", value=True)
        self.chrome_options.add_argument("--start-maximized")
        self.webdriver = webdriver.Chrome(options=self.chrome_options)

    def get_internet_speed(self):
        self.webdriver.get(SPEED_TEST_URL)

        go = self.webdriver.find_element(By.XPATH,
                                         value="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")

        sleep(5)

        go.click()

        sleep(60)

        download = self.webdriver.find_element(By.XPATH,
                                               value="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        upload = self.webdriver.find_element(By.XPATH,
                                             value="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text

        self.down = download
        self.up = upload

        print(f"Download: {download}")
        print(f"Upload: {upload}")

    def tweet_at_provider(self):
        # Open a new tab
        self.webdriver.execute_script("window.open('');")

        # Switch to the new tab
        self.webdriver.switch_to.window(self.webdriver.window_handles[1])

        # Open a different URL in the new tab
        self.webdriver.get(X_URL)

        sleep(30)

        email = self.webdriver.find_element(By.XPATH,
                                            value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
        email.send_keys(EMAIL)

        next_button = self.webdriver.find_element(By.XPATH,
                                                  value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]")
        next_button.click()

        sleep(3)

        password = self.webdriver.find_element(By.XPATH,
                                               value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password.send_keys(PASSWORD)

        login = self.webdriver.find_element(By.XPATH,
                                            value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button")
        login.click()

        sleep(10)

        tweet_input = self.webdriver.find_element(By.XPATH,
                                                  value="//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        tweet_input.send_keys(f"My download: {self.down} and upload: {self.up}")
