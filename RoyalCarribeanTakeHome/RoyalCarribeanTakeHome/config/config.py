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
