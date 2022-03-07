import requests
import xmltodict
from datetime import datetime
import random
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from mail_template.template import render_mail_template

def get_nse_announcements():
    r = requests.get("http://feeds.feedburner.com/nseindia/ann")
    data = xmltodict.parse(r.text)
    final = []
    time = None
    for item in data["rss"]["channel"]["item"]:
        time = datetime.strptime(item["pubDate"],"%a, %d %b %Y %H:%M:%S PST")
        final.append({
            "title": item["title"],
            "link": item["link"],
            "pubDate": item["pubDate"]
        })
    return (final[0:5],time.weekday())

def get_bse_notices():
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-US,en;q=0.9,hi;q=0.8,la;q=0.7",
        "if-modified-since": "Sat, 19 Feb 2022 04:07:23 GMT",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    r = requests.get("https://www.bseindia.com/data/xml/notices.xml",headers=headers)
    data = xmltodict.parse(r.content)
    final = []
    time = None
    items = data["rss"]["channel"]["item"]
    if type(items)==list:
        # single notice
        item = items
        time = datetime.strptime(item["pubDate"],"%a, %d %b %Y %H:%M:%S %Z")
        final.append({
            "title": item["title"],
            "link": item["link"],
            "pubDate": item["pubDate"]
        })
    else:
        for item in items:
            time = datetime.strptime(item["pubDate"],"%a, %d %b %Y %H:%M:%S %Z")
            final.append({
                "title": item["title"],
                "link": item["link"],
                "pubDate": item["pubDate"]
            })
    
    return (final[0:5],time.weekday())

mails = [
    {
        "email":"3528pratyush@gmail.com",
        "password": "ripwrydsyjvpjbfj"
    },
    {
        "email":"1863pratyush@gmail.com",
        "password": "huweyelhvftsjrkf"
    }
]

def send_mail(receiver_emails):
    current_time = datetime.now()

    if current_time.weekday() != 6:
        sender = random.choice(mails)
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Stocker Daily Update"
        msg["From"] = sender["email"]
        msg["To"] = sender["email"]
        msg["BCC"] = ", ".join(receiver_emails) 
        nse_announcements = get_nse_announcements()
        bse_notices = get_bse_notices()
        if nse_announcements[1] == current_time.weekday() and bse_notices[1] == current_time.weekday():
            html = render_mail_template(nse_announcements[0],bse_notices[0])

            part = MIMEText(html, "html")
            msg.attach(part)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender["email"], sender["password"])
                server.sendmail(sender["email"],receiver_emails,msg.as_string())
