"""
This script runs the RoyalCarribeanTakeHome application using a development server.
"""

from os import environ
from RoyalCarribeanTakeHome import app

if __name__ == '__main__':
    HOST = '127.0.0.1'
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
