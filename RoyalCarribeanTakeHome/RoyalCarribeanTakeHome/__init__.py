from flask import Flask
import sys
import os
import mysql.connector

# Add the path to your config folder to the sys.path list
config_path = os.path.join(os.path.dirname(__file__), 'config')
sys.path.append(config_path)

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Configure MySQL connection
cnx = mysql.connector.connect(
    user=Config.USERNAME,
    password=Config.PASSWORD,
    host=Config.CONNECTION_STRING,
    port=Config.PORT,
    database='RoyalCaribbeanDB'
)
# Create a cursor for executing SQL queries
cursor = cnx.cursor()
from . import views