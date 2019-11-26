from pathlib import Path
import sys

from pkg_scripts.db_management import Database
from pkg_scripts.pkg_installation import install_packages, install_requirements
from pkg_scripts.pkg_updation import update_packages
from pkg_scripts.pkg_uninstallation import uninstall_packages





def run_application():
    dbfile = Path("packages.db")
    database = Database()
    engine = database.engine
    db = database.packages

    if not dbfile.is_file():
        db, engine = database.initiate_engine()

    command = sys.argv[1]
    packages = sys.argv[2:]

    if command == "install" or command == "i":
        install_packages(packages, db, engine)

    elif command == "req" or command == 'r':
        install_requirements(db, engine)

    elif command == "uninstall" or command == "un":
        uninstall_packages(packages, db, engine)

    elif command == "update" or command == "up":
        update_packages(packages, db, engine)

    elif command == "help" or command == "h" or command == "?" or command is None:
        print("[+] Usage instructions:")
        print("""

    + Syntax:
    
    keepr <command> <package list>
    
    
    + Commands:
    
    * install - Install Packages
    * req - Install from requirements.txt
    * uninstall - Uninstall Packages and dependencies
    * update - Update an existing package
    * help - Display Help information
    * credits - List author credits
    
    
    + Example:    
    
    keepr install django==2.2 pymongo==1.2
    OR
    keepr req
            """)

    elif command == "credits" or command == "c":
        print(
            "This application was developed by:",
            "Sameeran Bandishti [sameeranbandishti@ieee.org]",
            "Ayush Priya [ayushpriya10@ieee.org]\n",
            "For any help or queries about the application, please contact the team at shopkeepr3.6@gmail.com",
            sep='\n'
        )

    else:
        print('[-] %s is not a command. Please use "help" to look at usage instructions.' % command)


if __name__ == "__main__":
    run_application()
