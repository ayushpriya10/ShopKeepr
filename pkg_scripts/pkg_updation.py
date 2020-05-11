from pkg_scripts.db_management import Requirements
from pkg_scripts.misc_functions import check_if_exists, install, get_version, update_requirements_file


def update_packages(packages_to_update, session):
    for package in packages_to_update:
        if '==' in package:
            package_name = package[:package.index("=")]
        else:
            package_name = package

        exists = check_if_exists(session, package_name)
        if exists:
            install(package)
            requirement_instance = session.query(Requirements.name.is_(package_name)).first()
            requirement_instance.version = get_version(package)
            session.commit()

        else:
            return False

    return update_requirements_file(session)

