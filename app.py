from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Config app
app = Flask(__name__)

# Config db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Create database
from Models import Contract, Email
db.create_all()

# Add controllers
from Controllers import *

# Config run
if __name__ == "__main__":
    app.run(debug=True)