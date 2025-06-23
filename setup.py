#!/usr/bin/env python3
"""
Setup script for the Mushroom Cultivation Quiz package.
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r', encoding='utf-8') as f:
        return f.read()

# Read requirements
def read_requirements():
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="mushroom-cultivation-quiz",
    version="2.0.1",
    author="Aaron J",
    author_email="git@aaronemail.xyz",
    description="A comprehensive educational quiz application for mushroom cultivation enthusiasts",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/aaronjacobs-chelt/mushroom-cultivation-quiz",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "mushroom-quiz=mushroom_quiz:main",
        ],
    },
    keywords="mushroom cultivation quiz education learning mycology",
    project_urls={
        "Bug Reports": "https://github.com/aaronjacobs-chelt/mushroom-cultivation-quiz/issues",
        "Source": "https://github.com/aaronjacobs-chelt/mushroom-cultivation-quiz",
        "Documentation": "https://github.com/aaronjacobs-chelt/mushroom-cultivation-quiz#readme",
    },
)
