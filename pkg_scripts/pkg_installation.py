import importlib

import pkg_resources

from pkg_scripts.db_management import Requirements
from pkg_scripts.misc_functions import check_if_exists, install, get_version, update_requirements_file
from pkg_scripts.pkg_updation import update_packages


def add_dependency(session, name, parent_id):
    package_instance = Requirements(name=name, version=get_version(name), parent_id=parent_id)
    session.add(package_instance)
    return


def add_package(session, package_name_with_version, package_name):
    print("Installing: " + package_name_with_version)
    install(package_name_with_version)

    package_instance = Requirements(name=package_name, version=get_version(package_name_with_version))

    session.add(package_instance)

    return package_instance.id


# Function to retrieve a list of the dependencies of the package
def get_dependencies(package_name):
    importlib.reload(pkg_resources)
    _package = pkg_resources.working_set.by_key[package_name]
    print("Looking for dependencies of: ")
    print(_package)
    return [str(r) for r in _package.requires()]


def perform_add_module(session, packages_to_install):
    for package_name_with_version in packages_to_install:
        if "==" in package_name_with_version:
            package_name = package_name_with_version[:package_name_with_version.index("=")]
            version = package_name_with_version[package_name_with_version.index("==") + 2:]
        else:
            package_name = package_name_with_version
            version = None
        print(package_name)
        print(version)
        exists = check_if_exists(session, package_name)
        if exists:
            update_packages(packages_to_update=[package_name_with_version], session=session)

        else:
            parent_id = add_package(session, package_name_with_version, package_name)
            dependencies = get_dependencies(package_name)
            for dep in dependencies:
                add_dependency(session, dep, parent_id)


def install_packages(Session, packages_to_install):
    session = Session()
    perform_add_module(session, packages_to_install)
    update_requirements_file(session)
    session.close()


def install_requirements(Session):
    requirements_file = open('requirements.txt', 'r')
    packages = requirements_file.readlines()
    install_packages(Session, packages)
