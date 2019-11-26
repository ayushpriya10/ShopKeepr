
import codecs
import os
import re

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

REQUIREMENTS = ['sqlalchemy']




try:
    fh = codecs.open("DESCRIPTION.md", encoding="utf-8")
    long_description = fh.read()
    fh.close()
except FileNotFoundError:
    long_description = ""

setup(
        name="shopkeepr",
        version="1.0.15",
        description="A command line tool for project management. Made for Developers",
        long_description=long_description,
        url="https://github.com/ayushpriya10/ShopKeepr",
        author="Sameeran Bandishti, Ayush Priya",
        author_email="shopkeepr3.6@gmail.com",
        packages=find_packages(include=[
            "pkg_scripts"
        ]),
        include_package_data=True,
        entry_points={
            "console_scripts": [
                'keepr = pkg_scripts.main:run_application'
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