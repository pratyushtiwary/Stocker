from conn import db

class Emails(db.Model):
    __tablename__ = "emails"
    email = db.Column(db.String(100),primary_key=True,nullable=False)

    def __init__(self,email):
        self.email = email

    @staticmethod
    def select_all():
        return Emails.query.all()

    @staticmethod
    def count_all():
        return Emails.query.count()