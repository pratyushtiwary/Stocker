from apscheduler.schedulers.blocking import BlockingScheduler
from utils import send_mail

import app
from conn import db
from model.Emails import Emails

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=11)
def scheduled_job():
    emails = Emails.select_all()
    if len(emails)>0:
        send_mail(emails)

if __name__ == "__main__":
    sched.start()