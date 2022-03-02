from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://Stocker:Eeg52pfJ6GQH@DK@Stocker.mysql.pythonanywhere-services.com:3306/Stocker$default" 

db = SQLAlchemy(app)