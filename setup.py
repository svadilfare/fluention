#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fluention",  # Replace with your own username
    version="0.0.1",
    author="Casper Weiss Bang",
    author_email="master@thecdk.net",
    description="Fluent interfaces for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/svadilfare/fluention",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
