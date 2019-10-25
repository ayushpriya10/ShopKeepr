import sys


from functions import *

# Opening the database
conn = engine.connect()
print("Database Opened")

# Collects names of packages to be uninstalled from terminal and stores them in an array
packages_to_uninstall = sys.argv[1:]

for package in packages_to_uninstall:
    parent_pid = check_if_exists(package)
    flag = True
    if parent_pid is not None:
        delete_dependencies(parent_pid)

    delete_package(package, parent_pid)
