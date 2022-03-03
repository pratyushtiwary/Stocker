from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://hrnzwmqqmvkwoh:85bfa7f9bd685f86776ade77d87735bf00616de6f6b3293f57b74e6011feea34@ec2-52-209-185-5.eu-west-1.compute.amazonaws.com:5432/d3dbos59a718p5" 

db = SQLAlchemy(app)