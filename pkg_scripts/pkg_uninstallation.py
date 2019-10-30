from pkg_scripts.misc_functions import open_database, check_if_exists, uninstall, delete_package, update_requirements_file


def delete_dependencies(conn, parent_pid, db):
    select_dependencies = db.select().where(db.c.parent_id == parent_pid)
    result = conn.execute(select_dependencies)
    print("Selected Dependencies:")
    # for _row in result:
    #     print(_row)

    flag = True

    for _row in result:
        common_dependencies = conn.execute(db.select().where(db.c.name == _row[1]))
        print(f"List of entries for the dependency {_row[1]}")
        # for _com_dep in  common_dependencies:
        #     print(_com_dep)

        for _com_dep in common_dependencies:
            if int(_com_dep[3]) != parent_pid:
                print(str(_com_dep[3]) + " " + str(parent_pid))
                flag = False

        if flag:
            print("uninstalling:")
            print(_row[1])
            uninstall(_row[1])

        delete_dependency = db.delete().where(db.c.pid == _row[0])
        conn.execute(delete_dependency)
        flag = True


def perform_remove_module(conn, packages_to_uninstall, db):
    for package in packages_to_uninstall:
        if '==' in package:
            package_name = package[:package.index('=')]
        else:
            package_name = package
        parent_pid_list = check_if_exists(conn, package_name, version=None, db=db)
        print("Pid List")
        print(parent_pid_list)
        if parent_pid_list is not None:
            for parent_pid in parent_pid_list:
                delete_dependencies(conn, parent_pid, db)
                delete_package(conn, package, parent_pid, db)
        else:
            print("Package has not been installed")


def uninstall_packages(packages_to_uninstall, db, engine):
    conn = open_database(engine)
    print("Connection Established with database")
    perform_remove_module(conn, packages_to_uninstall, db)
    print("Module Removed")
    update_requirements_file(conn, db)
    print("Update Requirements")
