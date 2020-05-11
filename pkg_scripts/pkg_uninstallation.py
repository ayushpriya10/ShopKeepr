from pkg_scripts.db_management import Requirements
from pkg_scripts.misc_functions import check_if_exists, uninstall, delete_package, update_requirements_file


def delete_dependencies(session, requirement_id):
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


def perform_remove_module(session, packages_to_uninstall):
    for package in packages_to_uninstall:
        if '==' in package:
            package_name = package[:package.index('=')]
        else:
            package_name = package
        exists = check_if_exists(session, package_name)
        if exists:
            parent_package_id = session.query(Requirements.id).filter(Requirements.name == package_name).first()
            for requirement_id in session.query(Requirements.parent_id.is_(parent_package_id)):
                delete_dependencies(session, requirement_id)
                delete_package(session, package, requirement_id)
        else:
            print("Package has not been installed")


def uninstall_packages(Session, packages_to_uninstall):
    session = Session()
    perform_remove_module(session, packages_to_uninstall)
    print("Module Removed")
    update_requirements_file(conn, db)
    print("Update Requirements")
    conn.close()
