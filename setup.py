from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="xxt",
    version="0.0.",
    description="Library with many uses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="Xi Teo",
    author_email="diamondraft1575@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ],
    packages=["xxt"],
    include_package_data=True,
    install_requires=["datetime", "openai"]
)