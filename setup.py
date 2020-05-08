#
# . ___ _              _    _        _  _ ___ _____
#  / __| |_  ___ __ __| |_ (_)__ _  | \| | __|_   _|
# | (__| ' \/ -_) _/ _| ' \| / _` |_| .` | _|  | |
#  \___|_||_\___\__\__|_||_|_\__,_(_)_|\_|___| |_|
#
# Created by Daniel Checchia on 23/04/2020 at 09:58
# CopyLeft (c) 2020 - GPLv3 - Checchia.NET (https://Checchia.NET)
#
import sys
from setuptools import setup, find_packages

if sys.version < '3.6':
    print("ERROR: python version 3.6 or higher is required")
    sys.exit(1)

setup(
  name='SimpleMongoMackup',
  packages = find_packages(),
  version='0.0.4',
  description='A simple MongoDB backup',
  author='Checchia.NET - IT Solutions',
  author_email='dono@checchia.net',
  license='GPLv3',
  install_requires = ["boto3"],
  url='https://github.com/checchia/SimpleMongoMackup', # The project's main homepage.
  keywords = ['MongoDB', 'backup', 'backup Rotate'], # arbitrary keywords
  classifiers = [
             "Development Status :: 5 - Production/Stable",
             "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
             "Operating System :: POSIX :: Linux",
             "Natural Language :: Portuguese (Brazilian)",
             "Programming Language :: Python :: 3.6",
             "Topic :: Database",
             ],
)
