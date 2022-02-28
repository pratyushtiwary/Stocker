from flask import Flask, request, Response
import json

app = Flask(__name__)


from conn import db
from model.Emails import Emails

db.create_all()

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