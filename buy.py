import sys

from sqlalchemy import select

from database import engine, packages
from functions import get_dependencies, add_package, add_dependency

# Opening the database
conn = engine.connect()
print("Database Opened")

# Collects names of packages to be installed from terminal and stores them in an array
packages_to_install = sys.argv[1:]
for package in packages_to_install:
    exists = select([packages.c.name]).where(packages.c.name == package)
    result = conn.execute(exists)

    if result.first() is None:
        pid = add_package(package)
        # Function to retrieve a list of the dependencies of the package
        dependencies = get_dependencies(package)
        for dep in dependencies:
            add_dependency(dep, pid)

