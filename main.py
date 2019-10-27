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

    print(sys.argv[1])