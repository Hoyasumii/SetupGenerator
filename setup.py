import os
from setuptools import setup

if os.path.isfile("README.md"):
    with open("README.md", "r", encoding="utf-8") as readme:
        long_description = readme.read()

setup(
    name="setup-generator",
    version=1.1,
    description="Pequena biblioteca para criar um setup.py rápido.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Alan Reis Anjos",
    author_email="alanreisanjo@gmail.com",
    url="https://github.com/Hoyasumii/SetupGenerator",
    packages=['setupGenerator', 'setupGenerator.scripts'],
    package_data={'setupGenerator': ['.template']},
    install_requires=['Jinja2==3.1.2', 'keyboard==0.13.5', 'MarkupSafe==2.1.3', 'python-slugify==8.0.1', 'setuptools==69.0.3', 'simple-form==1.4', 'text-unidecode==1.3'],
    license="GPL-3.0",
    entry_points={'console_scripts': [
        "setup-generator = setupGenerator.setupGenerator:setupGenerator"
    ]}
)