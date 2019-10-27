from misc_functions import open_database, check_if_exists, uninstall, delete_package, update_requirements_file


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
        else:
            print("Package has not been installed")

            return False


def sell(packages_to_uninstall, db, engine):
    conn = open_database(engine)
    perform_remove_module(conn, packages_to_uninstall, db)
    update_requirements_file(conn, db)


if __name__ == '__main__':
    sell(packages_to_uninstall=[], db="", engine="")
