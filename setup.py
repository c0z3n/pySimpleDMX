# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name="pysimpledmx",
    version="0.1.1",
    description="simple dmx control for the Enttec DMX USB Pro",
    license="GPLV3",
    author="c0z3n",
    url="https://github.com/c0z3n/pySimpleDMX",
    packages=find_packages(),
    install_requires=[
        "pyserial"
    ],
    long_description=open("README.md").read(),
    classifiers=[
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Other Audience",
        "Topic :: Artistic Software",
    ]
)
