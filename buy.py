from functions import *


def buy(packages_to_install, db, engine):
    # Opening the database
    conn = open_database(engine)

    perform_add_module(conn, packages_to_install, db)
