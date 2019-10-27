import pkg_resources

from misc_functions import open_database, check_if_exists, install, get_version, update_requirements_file


def add_dependency(conn, name, parent_pid, db):
    dependency_package_insert_query = db.insert().values(
        name=name,
        version=get_version(name),
        parent_id=parent_pid
    )

    conn.execute(dependency_package_insert_query)


def add_package(conn, package, db):
    check_if_exists(conn, package, db)
    install(package)
    primary_package_insert_query = db.insert().values(
        name=package,
        version=get_version(package),
        parent_id=None
    )
    
    result = conn.execute(primary_package_insert_query)
    
    return result.inserted_primary_key[0]

# Function to retrieve a list of the dependencies of the package
def get_dependencies(package):
    _package = pkg_resources.working_set.by_key[package]
    
    return [str(r) for r in _package.requires()]


def perform_add_module(conn, packages_to_install, db):
    for package in packages_to_install:
        exists = check_if_exists(conn, package, db)

        if exists is None:
            pid = add_package(conn, package, db)

            dependencies = get_dependencies(package)
            for dep in dependencies:
                add_dependency(conn, dep, pid, db)

        else:
            print("Package already installed")
            return False


def install_package(packages_to_install, db, engine):
    conn = open_database(engine)
    perform_add_module(conn, packages_to_install, db)
    update_requirements_file()


if __name__ == '__main__':
    buy(packages_to_install=[], db="", engine="")
