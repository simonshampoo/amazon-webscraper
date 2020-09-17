import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Cooler-Master-MasterLiquid-Chamber-MLA-D24M-A18PC-R1/dp/B07CRGC899/ref=sr_1_3?crid=27DW5B6SBZO0Y&dchild=1&keywords=pc+liquid+cooler&qid=1596674717&sprefix=pc+liquid+%2Caps%2C204&sr=8-3'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

def check_price():
    page = requests.get(URL, requests, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id ='priceblock_ourprice').get_text()
    converted_price = float(price[1:10])

    if (converted_price < 72.61):
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('simonshm5@gmail.com', 'alhmrwxpcmknbztz')

    subject = 'price lowered!'
    body = 'link : https://www.amazon.com/Cooler-Master-MasterLiquid-Chamber-MLA-D24M-A18PC-R1/dp/B07CRGC899/ref=sr_1_3?crid=27DW5B6SBZO0Y&dchild=1&keywords=pc+liquid+cooler&qid=1596674717&sprefix=pc+liquid+%2Caps%2C204&sr=8-3'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('simonshm5@gmail.com', 'simonshm5@gmail.com', msg)
    print("email has been sent")

    server.quit()

while (True):
    check_price()
    time.sleep(60*60*12)