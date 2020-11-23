# amazon-webscraper
**DEPRECATED**

It is against Amazon TOS to webscrape product data, and they recommend that you utilize AWS services to do so. It seems that there have been more measures to prevent data scraping. You can read more here: https://webservices.amazon.com/paapi5/documentation/register-for-pa-api.html

A simple webscraper that sends an email when the tracked product's price drops to a certain amount set by user. 

You will need your browser's user agents, URL of the item you want to track, the threshold price, and the recipient email. 

It will run in the background, sleeping the thread every 12 hours. 
