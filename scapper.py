import requests
from bs4 import BeautifulSoup 
import smtplib
import time

URL  = "https://www.amazon.co.uk/MSI-RTX-2070-SUPER-VENTUS/dp/B07TTSVC7K/ref=sr_1_3?keywords=nvidia&qid=1582824806&sr=8-3"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = int(price[1:-3])

    if(int(converted_price) < 400):
        send_mail()

    print(converted_price)

    if(int(converted_price) < 490): 
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email1', 'password')

    subject = 'RTX Price Drop!'
    body = 'Check https://www.amazon.co.uk/MSI-RTX-2070-SUPER-VENTUS/dp/B07TTSVC7K/ref=sr_1_3?keywords=nvidia&qid=1582824806&sr=8-3'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'email1',
        'email2',
        msg
    )
    print('An email has been sent.')

    server.quit()

while(True):
    check_price()
    time.sleep(172800)
