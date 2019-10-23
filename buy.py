import sqlite3
import sys

from functions import install, dependencies

conn = sqlite3.connect('packages.db')  # Opening the database
print("Database Opened")
packages_to_install = sys.argv[
                      1:]  # Collects names of packages to be installed from terminal and stores them in an array

for x in packages_to_install:
    install(x)  # Function to install the given packaged
    # conn.execute("INSERT INTO PACKAGES (PID, NAME, VERSION, PARENTID) VALUES ()") 
    # todo find a way to insert values into databases from variables
    dep = dependencies(x)  # Function to retrieve a list of the dependencies of the package
