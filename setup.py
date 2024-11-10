from distutils.core import setup
from setuptools import find_packages

setup(
    name="math_quiz",
    version="1.0",
    author="Ali",
    author_email="saif.ali@fau.de",
    packages=find_packages(),
    install_requires=["numpy", "turtles"],
)
