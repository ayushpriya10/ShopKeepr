import sqlite3
import sys

from functions import install, get_dependencies, get_version

conn = sqlite3.connect('packages.db')  # Opening the database
print("Database Opened")
packages_to_install = sys.argv[
                      1:]  # Collects names of packages to be installed from terminal and stores them in an array

for package in packages_to_install:
    install(package)  # Function to install the given packaged
    primary_package_insert_query = f"INSERT INTO PACKAGES (NAME, VERSION, PARENTID) VALUES ({package},{get_version(package)}, NULL)"
    conn.execute(primary_package_insert_query)
    get_pid_query = f"SELECT PID FROM PACKAGES WHERE NAME = {package}"
    pid = conn.execute(get_pid_query)
    print("pid: " + pid)
    dependencies = get_dependencies(package)  # Function to retrieve a list of the dependencies of the package
    for dep in dependencies:
        dependency_package_insert_query = f"INSERT INTO PACKAGES (NAME, VERSION, PARENTID) VALUES ({dep}, {get_version(dep)}, {pid})"
        conn.execute(dependency_package_insert_query)

