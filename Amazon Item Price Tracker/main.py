import smtplib
from email.message import EmailMessage
from pprint import pprint
import lxml
import requests
from bs4 import BeautifulSoup
import os

REGISTERED_PRICE = 100.00

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
DESTINATION_EMAIL = os.environ.get("DESTINATION_EMAIL")

item_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

response = requests.get(url=item_url, headers=header)
response.raise_for_status()
html = response.text
# pprint(response.text)

soup = BeautifulSoup(html, "html.parser")
# soup = BeautifulSoup(html, "lxml")
print(soup.prettify())

price_tag = soup.find(name="span", class_="a-offscreen")
price = float(price_tag.get_text().strip().split("$")[1])
product_title = soup.find(name="span", id="productTitle").get_text().strip()

print(f"Price: {price}")

if price < REGISTERED_PRICE:
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     msg = EmailMessage()
    #     message = f"Product:{product_title} is now {price}"
    #     msg.set_content(message)
    #     msg['subject'] = "Low price alert! "
    #     msg['to'] = DESTINATION_EMAIL
    #     msg['from'] = MY_EMAIL
    #     connection.starttls()
    #     connection.login(user=MY_EMAIL,
    #                      password=MY_PASSWORD)
    #     connection.send_message(msg)
    print(f"Product:{product_title} is now {price}")
