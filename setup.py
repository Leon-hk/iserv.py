from setuptools import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="",
    install_requires=requirements,
    version="0.1.0",
    description="Eine IServ Benutzer API",
    author="Captain_Sword123",
    license="MIT",
)