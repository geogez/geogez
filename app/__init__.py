from flask import Flask
from app.storage import database

app = Flask(__name__)

from app import routes
