#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
import subprocess

PKG="matikka"
name=PKG
version=subprocess.getoutput('git describe')
# version=version.replace("-", "+")
description="Matikkapeli"

if __name__ == "__main__":
    print(find_packages())
    setup(
        name=name,
        version=version,
        description=description,
        packages=find_packages(),
        python_requires='>=3.2',
        install_requires=[],
        entry_points='''
                [console_scripts]
                    {} = {}.matikka:main
            '''.format(name, PKG)
    )
