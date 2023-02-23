"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,request,jsonify,url_for,redirect
from . import app,cursor,cnx

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
    # Check if there's a delete_success variable in the query string
    delete_success = request.args.get('delete_success')
    error = request.args.get('error')
    success = request.args.get('success')
    person_id = request.args.get('person_id');

    # Set default values for nullable objects
    if not delete_success:
        delete_success = None
    if not error:
        error = None
    if not success:
        success = None
    if not person_id:
           person_id = None

        # If person_id is not None, fetch the record with that person_id
    employee = None
    if person_id:
        query = "SELECT * FROM Employees WHERE person_id = %s"
        cursor.execute(query, (person_id,))
        result = cursor.fetchone()
        if result:
            employee = {
                "person_id": result[0],
                "first_name": result[1],
                "last_name": result[2],
                "email_address": result[3],
                "hire_date": result[4].strftime('%Y-%m-%d'),
                "job_title": result[5],
                "agency_num": result[6],
                "registration_date": str(datetime.today())
            }

    return render_template(
        'index.html',
        title='Home Page',
        current_date=datetime.today().strftime('%Y-%m-%d'),
        delete_success=delete_success,
        error=error,
        success=success,
        employee=employee
    )



@app.route('/submit-employee', methods=['POST'])
def submit_employee():
    # Get the form data from the request object
    person_id = request.form.get('person_id')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email_address = request.form.get('email_address')
    hire_date = request.form.get('hire_date')
    job_title = request.form.get('job_title')
    agency_num = request.form.get('agency_num')
    registration_date = request.form.get('registration_date')

    # Check if the person_id is already in use
    query = "SELECT COUNT(*) FROM Employees WHERE person_id = %s"
    cursor.execute(query, (person_id,))
    count = cursor.fetchone()[0]
    if count > 0:
        return render_template(
        'index.html',
        title='Home Page',
        current_date = datetime.today().strftime('%Y-%m-%d'),
        error=f"Error: person ID {person_id} is already in use"
        )

    # Insert the employee data into the Employees table
    query = """
        INSERT INTO Employees
        (person_id, first_name, last_name, email_address, hire_date, job_title, agency_num, registration_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (person_id, first_name, last_name, email_address, hire_date, job_title, agency_num, registration_date)
    cursor.execute(query, values)
    cnx.commit()
    return redirect(url_for('home', success="you have successfully submitted an employee"))

@app.route('/api/employees', methods=['GET'])
def get_employees():
    # Execute a SELECT query on the Employees table
    query = "SELECT * FROM Employees"
    cursor.execute(query)

    # Fetch all results and build a list of employee dictionaries
    employees = []
    for row in cursor.fetchall():
        employee = {
            "person_id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "email_address": row[3],
            "hire_date": row[4].strftime('%Y-%m-%d'),
            "job_title": row[5],
            "agency_num": row[6],
            "registration_date": str(datetime.today())
        }
        employees.append(employee)

    return jsonify(employees)

@app.route('/delete/<id>', methods=['POST'])
def delete_employee(id):
    # Delete the employee with the given ID from the Employees table
    query = "DELETE FROM Employees WHERE person_id = %s"
    cursor.execute(query, (id,))
    cnx.commit()
    return redirect(url_for('home', delete_success="you have successfully deleted employee " + id))

@app.route('/edit/<id>',methods=['GET', 'POST'])
def edit_item(id):
        # code to get the item with the given ID from the database
    if request.method == 'POST':
        # code to update the item in the database with the new data from the form
        return f"Item with ID {id} has been updated"
    else:
        # code to render the edit form with the item data
         return redirect(url_for('home', person_id = id))
