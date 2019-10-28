import subprocess

import pkg_resources
from sqlalchemy import select, and_


def open_database(engine):
    conn = engine.connect()
    print("Database Opened")

    return conn


def install(package):  # Function to install the given packaged
    subprocess.run(["pip", "install", package])


def uninstall(package):
    subprocess.run(["pip", "uninstall", package, "-y"])


def delete_package(conn, package, pid, db):
    print(pid[0])
    query = db.delete().where(db.c.pid == pid[0])
    conn.execute(query)
    uninstall(package)


def check_if_exists(conn, package_name, version, db):
    if version is not None:
        package_exists = select([db.c.pid]).where(and_(db.c.name == package_name, db.c.version == version))
    else:
        package_exists = select([db.c.pid]).where(and_(db.c.name == package_name))

    result = conn.execute(package_exists)

    return result.fetchone()


def get_version(package):
    return pkg_resources.get_distribution(package).version


def update_requirements_file(conn, db):
    result = conn.execute(select([db.c.name, db.c.version]).where(db.c.parent_id is None))
    packages = []
    for _row in result:
        packages += [_row[0], _row[1]]

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
