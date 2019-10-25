import sys

from sqlalchemy import text, select
from database import engine, packages

from functions import *

conn = engine.connect()  # Opening the database
print("Database Opened")
packages_to_uninstall = sys.argv[
                      1:]  # Collects names of packages to be uninstalled from terminal and stores them in an array

for package in packages_to_uninstall:
    package_exists = select([packages.c.pid]).where(packages.c.name == package)
    result = conn.execute(package_exists)
    parent_pid = result.fetchone()[0]
    flag = True
    if parent_pid is not None:
        select_dependencies = packages.select().where(packages.c.parent_id == parent_pid)
        result = conn.execute(select_dependencies)
        for _row in result:
            common_dependencies = packages.select().where(packages.c.name == _row[1])
            for _com_dep in common_dependencies:
                if _com_dep[3] != parent_pid:
                    flag = False
            if flag:
                uninstall(_row[1])

            delete_dependency = packages.delete().where(packages.c.pid == _row[0])
            conn.execute(delete_dependency)

    delete_package = packages.delete().where(packages.c.pid == parent_pid)
    conn.execute(delete_package)
    uninstall(package)
