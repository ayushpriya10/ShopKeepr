import sys

from db_management import initiate_engine
from pkg_installation import buy
from pkg_updation import restock
from pkg_uninstallation import sell


# packages_to_install = sys.argv[1:]

# buy(packages_to_install, db, engine)

# packages_to_uninstall = sys.argv[1:]

# sell(packages_to_uninstall, db, engine)

if __name__ == "__main__":
    db, engine = initiate_engine()

    command = sys.argv[1]
    packages = sys.argv[2:]

    if command == "install" or command == "i":
        buy(packages, db, engine)
    
    elif command == "uninstall" or command == "un":
        sell(packages, db, engine)
    
    elif command == "update" or command == "up":
        restock(packages, db, engine)
    
    elif command == "help" or command == "h" or command == "?":
        print("[+] Usage instructions:")

        # TODO: add usage instructions
    
    else:
        print('[-] %s is not a command. Please use "help" to look at usage instructions.'%(command))