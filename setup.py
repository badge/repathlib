#!/usr/bin/env python
"""pathlib Package
"""
import re

from repathlib import Path
from setuptools import find_packages, setup


def find_version():
    """Get the current version of the package

    Returns
    -------
    str
        The current version of the package
    """

    here = Path(__file__).resolve().parent

    text = (here / "repathlib" / "__init__.py").read_text()

    version_match = re.search(
        pattern=r"^__version__ = ['\"]([^'\"]*)['\"]",
        string=text,
        flags=re.M
    )

    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='repathlib',
    version=find_version(),
    description='pathlib with regular expressions',
    author='Matthew Badger',
    url='https://github.com/badge/',
    packages=find_packages()
)
