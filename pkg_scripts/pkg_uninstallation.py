from pkg_scripts.db_management import Requirements
from pkg_scripts.misc_functions import check_if_exists, uninstall, delete_package, update_requirements_file


# Todo: Start from here
def delete_dependencies(session, requirement_id):
    dependencies = session.query(Requirements).filter(Requirements.parent_id == requirement_id).all().values(
        'name')
    # print("Selected Dependencies:")
    # for _row in result:
    #     print(_row)

    flag = True

    for dep in dependencies:
        common_dependencies = session.query(Requirements).filter(Requirements.name == dep).values('id')
        print(f"List of entries for the dependency {dep}")
        # for _com_dep in  common_dependencies:
        #     print(_com_dep)

        for _com_dep in common_dependencies:
            if _com_dep != requirement_id:
                print(str(_com_dep[3]) + " " + str(requirement_id))
                flag = False

        if flag:
            print("uninstalling:")
            print(dep)
            uninstall(dep)
            session.query(Requirements).filter(Requirements.name == dep).delete()

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
    update_requirements_file(session)
    print("Update Requirements")
    session.close()
