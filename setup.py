from distutils.core import setup
import py2exe
import sys

setup(
    version = "1.0",
    description = "csv operating",
    name = "Zhang Tao",

    # targets to build
    windows = ["csv_operating.py"],
    )