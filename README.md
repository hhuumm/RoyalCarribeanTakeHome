# Flask form 

![alt text](https://i.imgur.com/Yu27QYo.png)
![alt text](https://i.imgur.com/dxQIqZd.png)


# Designed for Royal Caribbean 
![alt text](https://i.imgur.com/3sIY60W.png)


[Click here to see it live](http://3.87.1.8:5000)


This is a repository for the Caribbean Cruise FullStack Software Engineer Role. The project is designed to demonstrate full CRUD functionality and match the criteria requested by the hiring managers.

# Technologies
The project is built using the following technologies:

HTML
CSS
JavaScript
Bootstrap
Python
Flask
MySQL

# Prerequisites
You must have a connection string, port and admin credentials to a mySQL database
Assuming your working on Linux, please refer to [microsoft documentation for starting a flask server](https://learn.microsoft.com/en-us/visualstudio/python/learn-flask-visual-studio-step-01-project-solution?view=vs-2022)

# SQL Scripts
Use this script to create the employee table
```SQL
CREATE TABLE Employee (
  person_id INT,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  email_address VARCHAR(100),
  hire_date DATE,
  job_title VARCHAR(100),
  agency_num INT,
  registration_date DATE
);
```

Use this script to populate the db with data
```SQL
INSERT INTO employee (person_id, first_name, last_name, email_address, hire_date, job_title, agency_num, registration_date) VALUES
  (1000001, 'John', 'Doe', 'johndoe@example.com', '2022-01-01', 'TA Rep A', 123, '2022-01-01'),
  (1000002, 'Jane', 'Smith', 'janesmith@example.com', '2022-02-01', 'TA Rep B', 456, '2022-02-01'),
  (1000003, 'Bob', 'Jones', 'bobjones@example.com', '2022-03-01', 'Direct Rep A', 789, '2022-03-01'),
  (1000004, 'Sarah', 'Lee', 'sarahlee@example.com', '2022-04-01', 'Direct Rep B', 101, '2022-04-01');

```

# Installation
Clone this repository to your local machine

Create your python virtual environment
```python3 -m venv env```

Activate your environment
```source env/bin/activate```


Install the required packages by running 
```pip install -r requirements.txt```


Start the Flask server by running 
```python runserver.py```


# Usage
Be sure to have your .env file set up with the proper variable names
```.env
USERNAME =
PASSWORD =
CONNECTION_STRING =
PORT =
```
# Run the server
The default port is set to http://localhost:5000/. 
From there, you can get, put, post , or delete an employee.
[Or just click here](http://3.87.1.8:5000)
