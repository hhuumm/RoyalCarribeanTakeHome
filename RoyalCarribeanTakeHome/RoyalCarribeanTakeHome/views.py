"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,request
from RoyalCarribeanTakeHome import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        current_date = datetime.today().strftime('%Y-%m-%d'),
    )

@app.route('/submit-employee', methods=['POST'])
def submit_employee():
    # Get the form data from the request object
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email_address = request.form.get('email_address')
    hire_date = request.form.get('hire_date')
    job_title = request.form.get('job_title')
    agency_num = request.form.get('agency_num')
    registration_date = request.form.get('registration_date')

    # Process the form data as needed (e.g. store in a database)
    # ...

    return 'Employee submitted successfully'