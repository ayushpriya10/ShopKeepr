import os
import subprocess
import sys

from pkg_scripts.misc_functions import check_if_exists, open_database, install


def check_virtualenv_installation(conn, db):
    exists = check_if_exists(conn, "virtualenv", "", db)
    if len(exists) == 0:
        answered = False
        while not answered:
            ans = input("Virtualenv has not been installed. Would you like to install it?")
            if ans.lower() == 'y' or ans.lower() == "yes":
                install("virutalenv")
                print("Installation complete. Setting environment up...")
                subprocess.run(["python3", "-m", "venv", "env"])
                answered = True
            elif ans.lower() == 'n' or ans.lower() == "no":
                print("Cannot activate environment without virtualenv.")
                answered = True
                exit()
            else:
                print("Invalid option.")
                answered = False

    else:
        if os.path.isdir('env'):
            return
        else:
            subprocess.run(["python3", "-m", "venv", "env"])


def activate_env(db, engine):
    conn = open_database(engine)
    check_virtualenv_installation(conn, db)
    subprocess.run(["source", "env/bin/activate"])
    print("Environment Activated.")
    conn.close()


def is_in_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))


def deactivate_env(db, engine):
    status = is_in_venv()
    if status:
        print("Deactivating environment...")
        subprocess.run(["deactivate"])
        print("Environment Deactivated")
    else:
        print("No active environments")
        exit()
