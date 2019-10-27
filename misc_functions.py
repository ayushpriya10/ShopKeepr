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