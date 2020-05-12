import importlib
import subprocess
import sys

import pkg_resources
from sqlalchemy import exists

from pkg_scripts.db_management import Requirements


def open_database(engine):
    conn = engine.connect()
    print("Database Opened")

    return conn


def install(package):  # Function to install the given packaged
    subprocess.run(["pip", "install", package])


def uninstall(package):
    subprocess.run(["pip", "uninstall", package, "-y"])


def delete_package(conn, package, pid, db):
    print(pid)
    query = db.delete().where(db.c.pid == pid)
    conn.execute(query)
    uninstall(package)


# Todo: Handle version numbers (Includes handling rollbacks to older versions)
def check_if_exists(session, package_name):
    if session.query(exists().where(Requirements.name == package_name)).scalar():
        return True
    else:
        return False


def get_version(package):
    print(f"Package is {package}")
    if "==" in package:
        print("Found ==  in package name")
        version = package[(package.index("==") + 2):]
        return version
    else:
        importlib.reload(pkg_resources)
        return pkg_resources.get_distribution(package).version


def update_requirements_file(session):
    packages = session.query(Requirements).values(Requirements.name, Requirements.version)
    string = ""
    for val in packages:
        print(val)
        if val[1]:
            string += val[0] + "==" + str(val[1])
        else:
            string += val[0]

        string += "\n"
    print("String = ")
    print(string)
    requirements_file = open('requirements.txt', 'w')
    requirements_file.write(string)
    requirements_file.close()


def is_in_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))
