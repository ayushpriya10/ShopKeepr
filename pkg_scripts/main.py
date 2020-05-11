from pathlib import Path
import sys

from pkg_scripts.db_management import Session, initialize_db
from pkg_scripts.environment_management import activate_env, deactivate_env
from pkg_scripts.pkg_installation import install_packages, install_requirements
from pkg_scripts.pkg_updation import update_packages
from pkg_scripts.pkg_uninstallation import uninstall_packages


INFORMATION = {
    'name': "shopkeepr",
    'version': "2.0.0",
}


def run_application():
    initialize_db()

    command = sys.argv[1]
    packages = sys.argv[2:]

    if command == "activate":
        activate_env()

    elif command == "deactivate":
        deactivate_env()

    elif command == "install" or command == "-i":
        install_packages(Session, packages)

    elif command == "req" or command == '-r':
        install_requirements(Session)

    elif command == "uninstall" or command == "-un":
        uninstall_packages(Session, packages)

    elif command == "update" or command == "-up":
        update_packages(packages, db, engine)

    elif command == '--version' or command == "-v":
        print(INFORMATION['version'])

    elif command == "--help" or command == "-h" or command == "?" or command is None:
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

    elif command == "--credits" or command == "-c":
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
