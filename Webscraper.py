import requests
from bs4 import BeautifulSoup
import smtplib
import time
import tkinter as tk
from tkinter import messagebox, Text


root = tk.Tk()
root.geometry("400x200")
root.title("Amazon Price Checker by Simon Shamoon")


user_input = tk.StringVar(root)

label = tk.Label(root, text="Enter your browser's user agent")
label.pack()
label1 = tk.Label(root, text="Enter URL of Amazon produict")
label1.pack()
label2 = tk.Label(root, text="We will email you when the price falls below")
label2.pack()
label3 = tk.Label(root, text="Please enter your email")
label3.pack()

headers = requests.utils.default_headers()
headers = tk.Entry(root, width = 40)
headers.pack()

url = tk.Entry(root, width = 40)
url.pack()

threshold = tk.Entry(root, width = 40)
threshold.pack()

recipient = tk.Entry(root, width = 40)
recipient.pack()

def check_price():
    page = requests.get(url.get(), requests, headers={'User-Agent': headers.get().strip()})
    soup = BeautifulSoup(page.content, 'lxml')
    
    try:
        title = soup.find(id='productTitle').get_text()
    except AttributeError:
        title = 'null'
        messagebox.showerror("Error", "Your item cannot currently be tracked.")


    try:
        price = soup.find(id ='priceblock_ourprice').get_text()
    except AttributeError:
        price = 0.000000
        messagebox.showerror("Error", "Your item cannot currently be tracked. This is probably due to Amazon blocking scripting on their site.")
    
    converted_price = float(price[1:4])
    print(converted_price)
    print(title.strip())

    if (converted_price < int(threshold.get())):
        send_mail()

    

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('simonshm5@gmail.com', 'alhmrwxpcmknbztz')

    subject = 'Your Item Has Fallen Under Your Desired Purchase Price'
    body = 'Link :' + url.get()
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('simonshm5@gmail.com', recipient.get(), msg)
    print("email has been sent")

    server.quit()


sendButton = tk.Button(root, text = "Submit And Close", command = check_price)
sendButton.pack()

tk.messagebox.showwarning(title = "Deprecation Warning", message = "This project is officially deprecated. Please use Amazon's API to get item data.\nYou can see more here: https://webservices.amazon.com/paapi5/documentation/register-for-pa-api.html")
root.mainloop()
 



while (True):
    check_price()
    time.sleep(60*60*12)

