"""
This module sets the setting of your database that is used to create a
connection with the database.
"""

"""Takes the a dictionary of the database configuration, that is host, password,
    and username
"""

DATABASE = {

    "host": "localhost",
    # This is not a secure password and is put here only for demonstration 
    # purposes
    "password": "12345678", 
    "user": "root",

}

"""This is the database name the database will use unless specified otherwise"""

DB_NAME = "defaultdbname1"