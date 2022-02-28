from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://rmhdyuxeswvqes:b282d8afe5db74f2eba2ce4e0eed1fa4ea3e0699e85dfa873e2a0527fa744038@ec2-54-74-102-48.eu-west-1.compute.amazonaws.com:5432/df3v6h4ef41leg" 

db = SQLAlchemy(app)