from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = "secret string"
db = SQLAlchemy(app)