from functions import *


def sell(packages_to_uninstall, db, engine):
    conn = open_database(engine)

    perform_remove_module(conn, packages_to_uninstall, db)


if __name__ == '__main__':
    sell(packages_to_uninstall=[], db="", engine="")
