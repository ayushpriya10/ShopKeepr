import subprocess

import pkg_resources
from sqlalchemy import select, create_engine, MetaData



def open_database(engine):
    conn = engine.connect()
    print("Database Opened")
    return conn


def install(package):  # Function to install the given packaged
    subprocess.run(["pip", "install", package], capture_output=True)


def add_package(conn, package, db):
    # Function to install the given packaged
    install(package)
    primary_package_insert_query = db.insert().values(name=package, version=get_version(package), parent_id=None)
    result = conn.execute(primary_package_insert_query)
    return result.inserted_primary_key[0]


def add_dependency(conn, name, parent_pid, db):
    dependency_package_insert_query = db.insert().values(name=name, version=get_version(name),
                                                         parent_id=parent_pid)
    conn.execute(dependency_package_insert_query)


def uninstall(package):
    subprocess.run(["pip", "uninstall", package], capture_output=True)


def delete_package(conn, package, pid, db):
    query = db.delete().where(db.c.pid == pid)
    conn.execute(query)
    uninstall(package)


def get_dependencies(package):  # Function to retrieve a list of the dependencies of the package
    _package = pkg_resources.working_set.by_key[package]
    return [str(r) for r in _package.requires()]


def get_version(package):
    return pkg_resources.get_distribution(package).version


def check_if_exists(conn, package, db):
    package_exists = select([db.c.pid]).where(db.c.name == package)
    result = conn.execute(package_exists)
    return result.fetchone()[0]


def delete_dependencies(conn, parent_pid, db):
    select_dependencies = db.select().where(db.c.parent_id == parent_pid)
    result = conn.execute(select_dependencies)
    flag = True
    for _row in result:
        common_dependencies = db.select().where(db.c.name == _row[1])
        for _com_dep in common_dependencies:
            if _com_dep[3] != parent_pid:
                flag = False
        if flag:
            uninstall(_row[1])

        delete_dependency = db.delete().where(db.c.pid == _row[0])
        conn.execute(delete_dependency)


def perform_remove_module(conn, packages_to_uninstall, db):
    for package in packages_to_uninstall:
        parent_pid = check_if_exists(conn, package, db)
        if parent_pid is not None:
            delete_dependencies(conn, parent_pid, db)
        delete_package(conn, package, parent_pid, db)


def perform_add_module(conn, packages_to_install, db):
    for package in packages_to_install:
        exists = check_if_exists(conn, package, db)

        if exists is None:
            pid = add_package(conn, package, db)

            # Function to retrieve a list of the dependencies of the package
            dependencies = get_dependencies(package)
            for dep in dependencies:
                add_dependency(conn, dep, pid, db)

