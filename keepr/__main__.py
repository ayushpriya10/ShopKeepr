from pathlib import Path
import click

from keepr.utils.db_management import Database
from keepr.utils.environment_management import activate_env
from keepr.utils.pkg_installation import install_packages, install_requirements
from keepr.utils.pkg_updation import update_packages
from keepr.utils.pkg_uninstallation import uninstall_packages
from keepr.utils.misc_functions import is_in_venv

INFORMATION = {
    'name': "shopkeepr",
    'version': "1.1.4",
}


class create_db(object):

    def __init__(self):
        """For creating an instance of db to be shared as context"""
        dbfile = Path('packages.db')
        database = Database()
        self.engine = database.engine
        self.db = database.packages

        if not dbfile.is_file():
            self.db, self.engine = database.initiate_engine()


@click.group(help='A CLI Tool for handling dangling dependencies')
@click.version_option(INFORMATION['version'])
@click.pass_context
def run_application(ctx):
    ctx.obj = create_db()


@run_application.command(help='Activating Virtual Environment')
@click.pass_context
def activate(ctx):
    activate_env()


@run_application.command()
@click.argument('packages', nargs=-1, type=str)
@click.option('--req', '-r', nargs=1, type=str,
              help="Install file using requirements file")
@click.option('--update', '-u', nargs=1, type=str,
              help="Update an existing packages")
@click.pass_context
def install(ctx, req, packages, update):
    """Install packages in the environemnt egs install pkg1==1.0 pkg2=1.0"""
    if is_in_venv():
        if req:
            install_requirements(ctx.obj.db, ctx.obj.engine)
        elif update:
            update_packages(packages, ctx.obj.db, ctx.obj.engine)
        elif packages:
            install_packages(packages, ctx.obj.db, ctx.obj.engine)
        else:
            click.echo("Give the package name to be installed")
    else:
        click.echo("Activate the environment first before installing packages")


@run_application.command()
@click.argument('packages', nargs=-1, type=str)
@click.pass_context
def uninstall(ctx, packages):
    """Uninstall Packages and dependencies egs uninstall pkg1==1.0 pkg2=1.0"""
    if is_in_venv():
        uninstall_packages(packages, ctx.obj.db, ctx.obj.engine)
    else:
        click.echo("Activate the environment first before uninstalling packages")


if __name__ == "__main__":
    run_application()
