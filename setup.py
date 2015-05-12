#! /usr/bin/env python
# -*- coding: utf-8 -*-

# setup.py --- Setup script for pythondialog
# Copyright (c) 2002, 2003, 2004, 2009, 2010, 2013, 2014, 2015  Florent Rougon
#
# This file is part of pythondialog.
#
# pythondialog is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# pythondialog is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston,
# MA  02110-1301 USA.

from __future__ import with_statement, unicode_literals, print_function
import os, sys, subprocess, traceback
from distutils.core import setup
from io import open


PACKAGE = "pythondialog"
# This is OK because dialog.py has no dependency outside the standard library.
from dialog import __version__ as VERSION

def main():

    with open("README.rst", "r", encoding="utf-8") as f:
        long_description = f.read()

    setup(name=PACKAGE,
          version=VERSION,
          description="A Python interface to the UNIX dialog utility and "
          "mostly-compatible programs (Python 2 backport)",
#         Doesn't work great with several authors...
          author="Robb Shecter, Sultanbek Tezadov, Florent Rougon, "
                 "Peter Åstrand",
          author_email="robb@acm.org, http://sultan.da.ru/, f.rougon@free.fr, "
                       "peter@cendio.se",
          maintainer="Florent Rougon",
          maintainer_email="f.rougon@free.fr",
          url="http://pythondialog.sourceforge.net/",
          download_url="http://sourceforge.net/projects/pythondialog/files/\
pythondialog/{version}/python2-{pkg}-{version}.tar.bz2".format(
            pkg=PACKAGE, version=VERSION),
          # Well, there isn't much UNIX-specific code in dialog.py, if at all.
          # I am putting Unix here only because of the dialog dependency...
          # Note: using the "Unix" case instead of "UNIX", because it is
          # spelled this way in Trove classifiers.
          platforms=["Unix"],
          long_description=long_description,
          keywords=["dialog", "ncurses", "Xdialog", "text-mode interface",
                    "terminal"],
          classifiers=[
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console :: Curses",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU Library or Lesser General Public "
            "License (LGPL)",
            "Operating System :: Unix",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Software Development :: User Interfaces",
            "Topic :: Software Development :: Widget Sets"],
          py_modules=["dialog"])

if __name__ == "__main__": main()
