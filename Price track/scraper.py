import requests
from bs4 import BeautifulSoup
import smtplib  
import time

URL = "https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_2?dchild=1&keywords=sony+a7&qid=1595052477&sr=8-2"

#The User-Agent request header is a characteristic string that lets servers and network peers identify the 
# application, operating system, vendor, and/or version of the requesting user agent.
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'} #gives info abt our browser

def check_price():
    page = requests.get(URL, headers=headers) #returns all the data from that website

    soup = BeautifulSoup(page.content, 'html.parser') #parse all the content in page and hence we can pull put individual pieces of info
    #print(soup.prettify())

    title = soup.find(id='productTitle').get_text()  #pulling out text in span content using its id which is = productTitle
    price=soup.find(id='priceblock_ourprice').get_text()  #string is returned

    converted_price = price[1:6]
    converted_price = float(converted_price.replace(",",""))

    if(converted_price < 1900):
        send_mail()

    print(title.strip()) #to remove empty spaces
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587) #establish a connectn b/w our connectn and gmail's connectn, connectn number is 587
    server.ehlo()  #extended helo,a command sent by an email server to identify itself when connecting to another email server to start the process of sending email
    server.starttls()  #.starttls() method to upgrade the connection to secure.i.e. encrypted
    server.ehlo()

    server.login('sushmithacg.20@gmail.com', 'cpdhesgfjagepgjd')

    subject = "Price fell down"
    body = "Check the amazon link https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_2?dchild=1&keywords=sony+a7&qid=1595052477&sr=8-2"

    #format the string with 'f'
    msg = f"Subject: {subject}\n\n{body}"
    sender = 'sushmithacg.20@gmail.com'
    receivers = ['2018cse_sushmithacg@nie.ac.in']
    server.sendmail(sender, receivers, msg)

    print("Hey, email has been sent!") 

    server.quit()


while(True):
    check_price()
    time.sleep(3600)