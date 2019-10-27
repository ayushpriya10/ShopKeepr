import pkg_resources
from sqlalchemy import select
import subprocess


def open_database(engine):
    conn = engine.connect()
    print("Database Opened")

    return conn


def install(package):  # Function to install the given packaged
    subprocess.run(["pip", "install", package], capture_output=True)


def uninstall(package):
    subprocess.run(["pip", "uninstall", package], capture_output=True)


def delete_package(conn, package, pid, db):
    query = db.delete().where(db.c.pid == pid)
    conn.execute(query)
    uninstall(package)


def check_if_exists(conn, package, db):
    package_exists = select([db.c.pid]).where(db.c.name == package)
    result = conn.execute(package_exists)
    
    return result.fetchone()[0]


def get_version(package):
    return pkg_resources.get_distribution(package).version


def update_requirements_file(db):
    # TODO: add relevant code to fetch all top level packages, then remove this comment.
    result = select([db.c.name, db.c.version]).where(db.c.parent_id == None)

    # Remove the below comment:
    '''
    assumed structure of name, version of the packages:
    packages = [
        [package_name, version],
        [package_name, version],
        ...
    ]
    '''

    string = str()

    for val in packages:
        if val[1]:
            string += val[0] + "==" + val[1]
        else:
            string += val[0]
        
        string += "\n"
    
    requirements_file = open('requirements.txt', 'w')
    requirements_file.write(string)
    requirements_file.close()