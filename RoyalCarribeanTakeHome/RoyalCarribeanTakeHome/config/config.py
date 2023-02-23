import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Use environment variables or default values
    USERNAME = "admin"
    PASSWORD = os.getenv('PASSWORD' )
    CONNECTION_STRING = os.getenv('CONNECTION_STRING')
    PORT = os.getenv('PORT')

    # Create database URI string
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{CONNECTION_STRING}:{PORT}/Database"
