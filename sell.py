from functions import *


def sell(packages_to_uninstall, db, engine):
    conn = open_database(engine)

    # Collects names of packages to be uninstalled from terminal and stores them in an array

    perform_remove_module(conn, packages_to_uninstall, db)
