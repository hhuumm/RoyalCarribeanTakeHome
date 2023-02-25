"""
This script runs the RoyalCarribeanTakeHome application using a development server.
"""


from RoyalCarribeanTakeHome import app

if __name__ == '__main__':
    HOST = '0.0.0.0'
    app.run(HOST, 5000)
