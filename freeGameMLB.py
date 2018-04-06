#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import smtplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from datetime import datetime

def send_email(text):
    
    FROM = my_email
    TO = my_email
    SUBJECT = text
    BODY = text
    message = 'Subject: {}\n\n{}'.format(SUBJECT, BODY)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(my_email, my_password)
    server.sendmail(FROM, TO, message)
    server.quit()

url = "https://www.mlb.com/live-stream-games/" + datetime.now().strftime("%Y/%m/%d")
my_team = "Mets"

f = open(os.path.dirname(os.path.abspath(__file__)) + "/email.txt","r")
my_email = f.read()
f.close()

f = open(os.path.dirname(os.path.abspath(__file__)) + "/pw.txt","r")
my_password = f.read()
f.close()

r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "lxml")

for row in soup.findAll("tr", class_="free-game"):
    teams = row.find("span", class_="card-title-teams").text
    if my_team in teams:
        send_email("The " + my_team + " game is the Free Game of the Day!")
        
for row in soup.findAll("div", class_="card-container facebook"):
    for row in row.findAll("span", class_="card-title-name"):
        if my_team in row.text:
            send_email("The " + my_team + " game is the Facebook Game of the Week!")

for div in soup.findAll("div", class_="card-container"):
    for span in div.findAll("span", class_="card-title-name"):
        if my_team in span.text:
            for div1 in div.findAll("div", class_="card-info mlbtv-card-info"):
                for span1 in div1.findAll("span", class_="card-info-link"):
                    if "ESPN" in span1.text:
                        send_email("The " + my_team + " game is on ESPN!")
                    elif "FOX" in span1.text:
                        send_email("The " + my_team + " game is on FOX!")
