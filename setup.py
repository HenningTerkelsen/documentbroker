# Copyright (C) 2012  Magenta ApS.
#
# Authors: Carsten Agger (carstena@magenta-aps.dk),
#          Dennis Isaksen (dennis@magenta-aps.dk),
#          Leif Lodahl (leif@magenta-aps.dk)
#
# This file is part of the Magenta Document Broker.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the Mozilla Public License for more details.

from setuptools import setup, find_packages

setup(
    name = "document_broker",
    version = open('VERSION').read().strip(),
    author = "Carsten Agger",
    author_email = "carstena@magenta-aps.dk",
    description = "Magenta Document Broker",
    url = "http://www.magenta-aps.dk",
    license="Mozilla Public License, version 2", 
    packages=['document_broker', 'document_templates'],
    long_description=open('README').read(),
    include_package_data = True
)
