import subprocess

import pkg_resources
from sqlalchemy import select

from database import packages, engine

conn = engine.connect()


def install(package):  # Function to install the given packaged
    subprocess.run(["pip", "install", package], capture_output=True)


def add_package(package):
    # Function to install the given packaged
    install(package)
    primary_package_insert_query = packages.insert().values(name=package, version=get_version(package), parent_id=None)
    result = conn.execute(primary_package_insert_query)
    return result.inserted_primary_key[0]


def add_dependency(name, parent_pid):
    dependency_package_insert_query = packages.insert().values(name=name, version=get_version(name), parent_id=parent_pid)
    conn.execute(dependency_package_insert_query)

def uninstall(package):
    subprocess.run(["pip", "uninstall", package], capture_output=True)


def delete_package(package, pid):
    query = packages.delete().where(packages.c.pid == pid)
    conn.execute(query)
    uninstall(package)


def get_dependencies(package):  # Function to retrieve a list of the dependencies of the package
    _package = pkg_resources.working_set.by_key[package]
    return [str(r) for r in _package.requires()]


def get_version(package):
    return pkg_resources.get_distribution(package).version


def check_if_exists(package):
    package_exists = select([packages.c.pid]).where(packages.c.name == package)
    result = conn.execute(package_exists)
    return result.fetchone()[0]


def delete_dependencies(parent_pid):
    select_dependencies = packages.select().where(packages.c.parent_id == parent_pid)
    result = conn.execute(select_dependencies)
    flag = True
    for _row in result:
        common_dependencies = packages.select().where(packages.c.name == _row[1])
        for _com_dep in common_dependencies:
            if _com_dep[3] != parent_pid:
                flag = False
        if flag:
            uninstall(_row[1])

        delete_dependency = packages.delete().where(packages.c.pid == _row[0])
        conn.execute(delete_dependency)
