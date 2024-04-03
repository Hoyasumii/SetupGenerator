import subprocess, os

def getPipFreeze():

    # Get Virtual Enviroment name
    venv = os.environ.get("VIRTUAL_ENV")


    if venv is not None:
        venv = venv.split("\\")[-1] if os.name == "nt" else venv.split("/")[-1]

        install_requires = None
        
        if os.name == "nt":
            install_requires = subprocess.run([f".\\{ venv }\\Scripts\\python", "-m", "pip", "freeze"], capture_output=True)
        else:
            install_requires = subprocess.run([f"./{ venv }/bin/python", "-m", "pip", "freeze"], capture_output=True)
    
    else:
        if os.name == "nt":
            install_requires = subprocess.run(["python", "-m", "pip", "freeze"], capture_output=True)
        else:
            install_requires = subprocess.run(["python3", "-m", "pip", "freeze"], capture_output=True)

    install_requires = install_requires.stdout.decode("utf-8").split("\n")
    install_requires = [ package[:-1] for package in install_requires if package != "" ]

    return install_requires
