from flask import Flask, request, Response
import hashlib
import json
from utils import send_mail

app = Flask(__name__)


from conn import db
from model.Emails import Emails

db.create_all()

@app.route("/api/sendMails",methods=["GET","POST"])
def send_mails():
    if request.method == "POST":
        token = request.headers.get("token")
        if hashlib.sha256(bytes(token,"utf-8")).hexdigest() == "bb7714c0c3b8bcdedfbacb759266f027dfdbf39cdb80a3e0d6c40788d876c886":
            emails = Emails.select_all()
            final = []
            for email in emails:
                final.append(email.email)
            if len(final)>0:
                send_mail(final)
                return Response(json.dumps({"status":"success"}),status=200,mimetype="application/json")
            else:
                return Response(json.dumps({"status":"error","message":"No emails found"}),status=200,mimetype="application/json")
        else:
            return Response(json.dumps({"status":"error","message":"Invalid token"}),status=400,mimetype="application/json")
    else:
        return Response(json.dumps({"status":"error","message":"Invalid request"}),status=400,mimetype="application/json")


@app.route('/api/save',methods=["GET","POST"])
def save_email():
    if request.method == "POST":
        data = request.get_json()
        email = data["email"]
        exists = Emails.query.filter_by(email=email).first()
        if exists:
            return Response(json.dumps({
                "status":False,
                "msg": "Email already exists!"
            }),status=400,mimetype="application/json")
        total_count = Emails.count_all()
        if total_count >= 100:
            return Response(json.dumps({
                "status":False,
                "msg": "Maximum limit reached!"
            }),status=400,mimetype="application/json")
        user = Emails(email)
        db.session.add(user)
        db.session.commit()
        return Response(json.dumps({
            "success": True,
            "msg": "Email saved successfully!"
        }),status=200,mimetype="application/json")
    return Response(json.dumps({
        "status":False,
        "msg": "Invalid Request"
    }),status=400,mimetype="application/json")

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)