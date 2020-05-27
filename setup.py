
import codecs
import os
import re

from setuptools import setup, find_packages

REQUIREMENTS = ['sqlalchemy','click']

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

def get_long_description():
    try:
        with codecs.open("DESCRIPTION.md", encoding="utf-8") as fh:
            long_description = fh.read()
        return long_description
    except FileNotFoundError:
        return "" 


setup(
        name="shopkeepr",
        version=get_version('VERSION.txt'),
        description="A command line tool for project management. Made for Developers",
        long_description=get_long_description(),
        url="https://github.com/ayushpriya10/ShopKeepr",
        author="Sameeran Bandishti, Ayush Priya",
        author_email="shopkeepr3.6@gmail.com",
        packages=find_packages(include=[
            "keepr", "keepr.utils", "keepr.utils.scripts"
        ]),
        include_package_data=True,
        entry_points={
            "console_scripts": [
                'keepr = keepr.__main__:run_application'
            ]
        },
        classifiers=[
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: MIT License ",
            "Programming Language :: Python :: 3.6",
        ],
        install_requires=REQUIREMENTS,
        keywords='pip requirements automation'
)