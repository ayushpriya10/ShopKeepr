import sys

from buy import buy
from database import initiate_engine
from sell import sell

db, engine = initiate_engine()

packages_to_install = sys.argv[1:]

buy(packages_to_install, db, engine)

packages_to_uninstall = sys.argv[1:]

sell(packages_to_uninstall, db, engine)
