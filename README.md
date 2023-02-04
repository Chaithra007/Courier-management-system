# Courier-management-system

The main objective of the Project on courier management system is to manage the details of 
Courier, Customer, Payment , Shipping and tracking of order. The purpose of the project is to 
build an application program to reduce the manual , work for managing the Courier , 
Customer , Delivery . It tracks all the details about delivery. The project is built end and only the administrator is guaranteed the access . The main purpose of this system is to connect all branches to the central database so the everywhere information is the same.

INSTALLATIONS:

Python: https://www.python.org/downloads/ <br>
Pycharm: https://www.jetbrains.com/pycharm/download/#section=windows <br>
Streamlit: pip install streamlit <br>
MySQL: https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/ <br>
Mysql connector: pip install mysql-connector-python <br>

CONNECTING THE APPLICATION TO A MYSQL SERVER

App.py

import mysql.connector <br>
mydb = mysql.connector.connect( <br>
host="localhost", <br>
user="root", <br>
password="" <br>
) <br>
c = mydb.cursor() <br>
c.execute("CREATE DATABASE courier") <br>

Run this part of the code once (streamlit run app.py) and then comment the 
code since this code is to create the database 'courier'

CREATING THE PYTHON APPLICATION FOR CRUD OPERATIONS

1. app.py file acts as the main function that calls other functions like 
create(),read(), update() and delete() which have been written as 
separate files for clarity.

2. create.py: Streamlit provides various user friendly functions like 
columns, selectbox etc which can be used to create an interactive UI.

3. read.py: In this file, you can view all the details that were add through 
the create file

4. update.py: In this file, you can update the details of a selected item that 
already exists in the database and see the changes in the UI itself


Run the command streamlit run app.py
