import os, subprocess
from setuptools import find_packages, setup
from TypedInput import typedInput
from KeyboardManager import listenKeyboard
from slugify import slugify

def setupGenerator():

    clear = lambda: os.system('cls') if os.name == 'nt' else os.system('clear')

    clear()
    print("Creating setup.py file...")

    name = slugify(typedInput("1. Project name: ", str))

    version = typedInput("2. Project version: (1.0) ", float, 1.0)

    description = typedInput("3. Project description: ", str)

    long_description = ""
    if os.path.isfile("README.md"):
        with open("README.md", "r", encoding="utf-8") as readme:
            long_description = readme.read()

    author = typedInput("4. Project author: ", str)

    author_email = typedInput("5. Project author email: ", str)

    url = typedInput("6. Project url: ", str)

    license = typedInput("7. Project license: ", str)
    
    clear()

    packages = find_packages()

    install_requires = subprocess.run(["python", "-m", "pip", "freeze"], capture_output=True).stdout.decode("utf-8").split("\n")
    install_requires = [ package[:-1] for package in install_requires if package != "" ]

    entry_points = { 'console_scripts': [ ] }
    
    with open("setup.py", "w", encoding="utf-8") as setupFile:

        setupFile.write(
f"""from setuptools import setup

setup(
    name="{name}",
    version={version},
    description="{description}",
    long_description=\"\"\"{long_description}\"\"\",
    long_description_content_type="text/markdown",
    author="{author}",
    author_email="{author_email}",
    url="{url}",
    packages={packages},
    install_requires={install_requires},
    license="{license}",
    entry_points={entry_points}
)
""")

if __name__ == "__main__":
    setupGenerator()