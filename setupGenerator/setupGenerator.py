import os
from setuptools import find_packages
from slugify import slugify
from simpleForm import Form
from jinja2 import Template
from .scripts.getPipFreeze import getPipFreeze

def setupGenerator():

    libPath = os.path.dirname(os.path.realpath(__file__))
    setupValues = Form("Setup Generator", spacing=2)

    setupValues.add (

        name={
            "type": str,
            "description": "Project name",
            "default": os.path.basename(os.getcwd())
        },
        version={
            "type": float,
            "description": "Project version",
            "default": 1.0
        },
        description={
            "type": str,
            "description": "Project description"
        },
        author={
            "type": str,
            "description": "Project author"
        },
        author_email={
            "type": str,
            "description": "Project author email",
            "validate": r"^[a-zA-Z0-9\._]{4,}@\w.{2,}\w{2,}$"
        },
        url={
            "type": str,
            "description": "Project url",
            "validate": r"^(https?|ftp):\/\/(-\.)?([a-zA-Z0-9]+(\.[a-zA-Z]{2,})+|([0-9]{1,3}\.){3}[0-9]{1,3})(:[0-9]{1,5})?(\/[a-zA-Z0-9._%+-]*)*(\?[a-zA-Z0-9+&%=]+(#[a-zA-Z0-9_]+)?)?$"
        },
        license={
            "type": str,
            "description": "Project license",
            "default": "GPL-3.0"
        }
    )

    setupValues()
    data = setupValues.values

    data['name'] = slugify(data['name'])

    if os.path.isfile("README.md"):
        with open("README.md", "r", encoding="utf-8") as readme:
            data['long_description'] = True

    data['packages'] = find_packages()
    data['package_data'] = { key: [ item for item in os.listdir(key.replace('.', '/')) if not item.endswith(".py") and os.path.isfile(f"{os.getcwd()}\\{ key }\\{ item }") ] for key in data['packages'] }

    data['install_requires'] = getPipFreeze()
    data['entry_points'] = { 'console_scripts': [ ] }

    templateFileName = f"{ libPath }\\.template" if os.name == "nt" else f"{ libPath }/.template"

    with open(templateFileName, "r", encoding="utf-8") as templateFile:
        template = Template(templateFile.read())

    output = template.render(data)

    with open("setup.py", "w", encoding="utf-8") as setupFile:
        setupFile.write(output)

if __name__ == "__main__":
    setupGenerator()
