from utils import send_mail

import app
from conn import db
from model.Emails import Emails


def main():
    emails = Emails.select_all()
    final = []
    for email in emails:
        final.append(email.email)
    if len(emails)>0:
        send_mail(final)

if __name__ == "__main__":
    main()