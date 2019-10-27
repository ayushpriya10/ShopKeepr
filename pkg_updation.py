from misc_functions import check_if_exists, install, get_version


def restock(packages_to_update, db, conn):
    for package in packages_to_update:
        pid = check_if_exists(package)
        
        if pid is not None:
            install(package)
            update_package_query = db.update().values(version=get_version(package)).where(db.c.name == package)
            conn.execute(update_package_query)
        
            return True
        
        else:
            return False

