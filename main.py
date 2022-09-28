import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


#Create Tables

create_admissions = """
CREATE TABLE Admissions(
patient_ID int primary key,
patient_name VARCHAR(50) NOT NULL,
patient_dob VARCHAR(50) NOT NULL,
patient_insurance VARCHAR(50) NOT NULL,
contact_number VARCHAR(20) NOT NULL,
patient_email VARCHAR(30) NOT NULL,
patient_reason VARCHAR(100) NOT NULL);
"""



create_table2 = """
create table Anesthetics_Staff(
Employee_ID int primary key,
Employee_Name varchar(30) not null,
Employee_Education varchar(20) not null,
Employee_Hiring_Date varchar(10) not null,
Employee_Salary varchar(15) not null,
Employee_Schedule varchar(10) not null,
Employee_eBenefits varchar(3) not null);"""

create_table3 = """
create table Cardiology_Staff(
Employee_ID int primary key,
Employee_Name varchar(30) not null,
Employee_Education varchar(20) not null,
Employee_Hiring_Date varchar(10) not null,
Employee_Salary varchar(15) not null,
Employee_Schedule varchar(10) not null,
Employee_eBenefits varchar(3) not null);"""

create_table4 = """
create table September_Cardiology_Appointments(
Appointment_ID int primary key,
Appointment_Date varchar(10) not null,
Appointment_Time varchar(10) not null,
Patient_Name varchar(30) not null,
Doctor_Name varchar(30) not null,
Completed varchar(20) not null);"""




#Callout section

connection = create_server_connection("localhost", "root", "student","Central_Clinic")
execute_query(connection, create_table4)
