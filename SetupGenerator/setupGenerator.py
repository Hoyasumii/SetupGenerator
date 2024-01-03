import os, subprocess
from setuptools import find_packages, setup
from TypedInput import typedInput
from KeyboardManager import listenKeyboard
from slugify import slugify

def setupGenerator():

    clear = lambda: os.system('cls') if os.name == 'nt' else os.system('clear')

    clear()
    print("Creating setup.py file...")

    name = typedInput("1. Project name: ", str)

    if name != None:
        name = slugify(name)

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

    # Get Virtual Enviroment name
    venv = os.environ.get("VIRTUAL_ENV")

    if venv is not None:
        venv = venv.split("\\")[-1]

        install_requires = None
        
        if os.name == "nt":
            install_requires = subprocess.run([f".\\{ venv }\\Scripts\\python", "-m", "pip", "freeze"], capture_output=True)
        else:
            install_requires = subprocess.run(["source", f"./{ venv }/bin/python", "-m", "pip", "freeze"], capture_output=True)
    
    else:
        if os.name == "nt":
            install_requires = subprocess.run(["python", "-m", "pip", "freeze"], capture_output=True)
        else:
            install_requires = subprocess.run(["python3", "-m", "pip", "freeze"], capture_output=True)

    install_requires = install_requires.stdout.decode("utf-8").split("\n")
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