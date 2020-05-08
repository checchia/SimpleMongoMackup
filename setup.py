#
# . ___ _              _    _        _  _ ___ _____
#  / __| |_  ___ __ __| |_ (_)__ _  | \| | __|_   _|
# | (__| ' \/ -_) _/ _| ' \| / _` |_| .` | _|  | |
#  \___|_||_\___\__\__|_||_|_\__,_(_)_|\_|___| |_|
#
# Created by Daniel Checchia on 23/04/2020 at 09:58
# Copyright (c) 2020 - Checchia.NET (https://Checchia.NET)
#
import pathlib
script_dir = pathlib.Path(__file__).parent.resolve()

from distutils.core import setup
setup(
  name='SimpleMongoMackup',
  packages = ['SimpleMongoMackup'], # this must be the same as the name above
  version='0.0.1',
  description='A simple MongoDB backup',
  author='Checchia.NET - IT Solutions',
  author_email='dono@checchia.net',
  license='GPLv3',
  url='https://github.com/checchia/SimpleMongoMackup', # The project's main homepage.
  keywords = ['MongoDB', 'backup', 'backup Rotate'], # arbitrary keywords
  classifiers = [],
)
