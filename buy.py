import sys

from sqlalchemy import text, select

from database import engine, packages
from functions import install, get_dependencies, get_version

conn = engine.connect()  # Opening the database
print("Database Opened")
packages_to_install = sys.argv[
                      1:]  # Collects names of packages to be installed from terminal and stores them in an array

for package in packages_to_install:
    exists = select([packages.c.name]).where(packages.c.name == package)
    result = conn.execute(exists)

    if result.first() is None:
        install(package)  # Function to install the given packaged
        primary_package_insert_query = packages.insert().values(name=package, version=get_version(package), parent_id=None)
        result = conn.execute(primary_package_insert_query)
        pid = result.inserted_primary_key[0]
        dependencies = get_dependencies(package)  # Function to retrieve a list of the dependencies of the package
        for dep in dependencies:
            dependency_package_insert_query = packages.insert().values(name=dep, version=get_version(dep), parent_id=pid)
            conn.execute(dependency_package_insert_query)

