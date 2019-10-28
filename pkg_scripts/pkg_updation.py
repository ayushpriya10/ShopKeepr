from pkg_scripts.misc_functions import check_if_exists, install, get_version, update_requirements_file


def update_packages(packages_to_update, db, conn):
    for package in packages_to_update:
        package_name = package[:package.index("=")]

        pid = check_if_exists(conn, package_name, version=None, db=db)
        print("pid = ")
        print(pid)
        if pid is not None:
            install(package)
            update_package_query = db.update().values(version=get_version(package_name)).where(db.c.name == package_name)
            conn.execute(update_package_query)
        
            return True
        
        else:
            return False
    
    update_requirements_file(conn, db)

