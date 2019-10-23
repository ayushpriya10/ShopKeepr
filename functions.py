import subprocess

import pkg_resources


def install(package):  # Function to install the given packaged
    subprocess.call(["pip", "install", package])


def dependencies(package):  # Function to retrieve a list of the dependencies of the package
    _package = pkg_resources.working_set.by_key[package]
    return [str(r) for r in _package.requires()]
