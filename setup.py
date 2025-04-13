from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = "Hotel Prediction",
    version = "0.1",
    author = "Udaykumar Gajavalli",
    packages = find_packages(),
    install_requires = requirements,

)