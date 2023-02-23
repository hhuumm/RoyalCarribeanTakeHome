"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,request,jsonify,url_for
from RoyalCarribeanTakeHome import app

class Employee:
    def __init__(self, person_id, first_name, last_name, email_address, hire_date, job_title, agency_num=None):
        self.person_id = person_id
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.hire_date = hire_date
        self.job_title = job_title
        self.agency_num = agency_num
        self.registration_date = datetime.date.today()


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        current_date = datetime.today().strftime('%Y-%m-%d')
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

@app.route('/api/employees', methods=['GET'])
def get_employees():
    # create a list of employees
    employees = [
        {
            "person_id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "email_address": "johndoe@example.com",
            "hire_date": "2020-01-01",
            "job_title": "Software Engineer",
            "agency_num": None,
            "registration_date": str(datetime.today())
        },
        {
            "person_id": 2,
            "first_name": "Jane",
            "last_name": "Doe",
            "email_address": "janedoe@example.com",
            "hire_date": "2021-01-01",
            "job_title": "Data Scientist",
            "agency_num": None,
            "registration_date": str(datetime.today())
        }
    ]

    return jsonify(employees)

@app.route('/delete/<id>',methods=['DELETE'])
def delete_employee(id):
     # code to delete the item with the given ID from the database
    return f"Deleted item with ID {id}"

@app.route('/edit/<id>',methods=['GET', 'POST'])
def edit_item(id):
        # code to get the item with the given ID from the database
    if request.method == 'POST':
        # code to update the item in the database with the new data from the form
        return f"Item with ID {id} has been updated"
    else:
        # code to render the edit form with the item data
        return render_template('edit.html', employee="")
