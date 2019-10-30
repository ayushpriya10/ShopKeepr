import importlib

import pkg_resources

from pkg_scripts.misc_functions import open_database, check_if_exists, install, get_version, update_requirements_file
from pkg_scripts.pkg_updation import update_packages


def add_dependency(conn, name, parent_pid, db):
    dependency_package_insert_query = db.insert().values(
        name=name,
        version=get_version(name),
        parent_id=parent_pid
    )

    conn.execute(dependency_package_insert_query)


def add_package(conn, package, package_name,  db):
    print("Installing: " + package)
    install(package)
    primary_package_insert_query = db.insert().values(
        name=package_name,
        version=get_version(package),
        parent_id=None
    )

    result = conn.execute(primary_package_insert_query)

    return result.inserted_primary_key[0]


# Function to retrieve a list of the dependencies of the package
def get_dependencies(package_name):
    importlib.reload(pkg_resources)
    _package = pkg_resources.working_set.by_key[package_name]
    print("Looking for dependencies of: ")
    print(_package)
    return [str(r) for r in _package.requires()]


def perform_add_module(conn, packages_to_install, db):
    for package in packages_to_install:
        if "==" in package:
            package_name = package[:package.index("=")]
            version = package[package.index("==")+2:]
        else:
            package_name = package
            version = None
        print(package_name)
        print(version)
        exists = check_if_exists(conn, package_name, version=None, db=db)
        if len(exists) == 1:
            update_packages(packages_to_update=[package], db=db, conn=conn)

        if len(exists) == 0:
            pid = add_package(conn, package, package_name, db)

            dependencies = get_dependencies(package_name)
            for dep in dependencies:
                add_dependency(conn, dep, pid, db)

        else:
            print("Package already installed")
            return False


def install_packages(packages_to_install, db, engine):
    conn = open_database(engine)
    perform_add_module(conn, packages_to_install, db)
    update_requirements_file(conn, db)



