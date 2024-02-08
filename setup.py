from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="dbt-rag-tools",
    version="0.1.1",
    description="A set of utilities to enable RAG for dbt projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://dbt-rag-tools.readthedocs.io/",
    author="Pragun Bhutani",
    author_email="bhutani.pragun@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ],
    packages=["dbt_rag_tools"],
    include_package_data=True,
    install_requires=["pyyaml", "typing_extensions"]
)