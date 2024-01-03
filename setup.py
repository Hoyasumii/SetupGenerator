from setuptools import setup

setup(
    name="hoy-setup-generator",
    version=1.0,
    description="Pequena biblioteca para criar um setup.py rápido.",
    long_description="""## [SetupGenerator](https://pypi.org/project/hoy-setup-generator/)
- Pequena biblioteca para criar um setup.py rápido.
- Clique [**aqui**](https://github.com/Hoyasumii/SetupGenerator) para acessar o repositório.
---
## Instalação
- Você pode baixar pelo pip:
```
pip install hoy-setup-generator
```
---
## Como usar?
- Abra o terminal e digite:
```
setup-generator 
```
- Depois disso, você será solicitado a digitar o nome do seu projeto, o nome do autor, a versão do projeto, a descrição do projeto, o nome do arquivo principal e o nome do arquivo de instalação. Após isso, o arquivo setup.py será criado.""",
    long_description_content_type="text/markdown",
    author="Alan Reis Anjos",
    author_email="alanreisanjo@gmail.com",
    url="https://github.com/Hoyasumii/SetupGenerator",
    packages=['SetupGenerator'],
    install_requires=['argcomplete==3.2.1', 'certifi==2023.11.17', 'charset-normalizer==3.3.2', 'click==8.1.7', 'colorama==0.4.6', 'docutils==0.20.1', 'idna==3.6', 'importlib-metadata==7.0.1', 'jaraco.classes==3.3.0', 'keyring==24.3.0', 'markdown-it-py==3.0.0', 'mdurl==0.1.2', 'more-itertools==10.1.0', 'nh3==0.2.15', 'packaging==23.2', 'pkginfo==1.9.6', 'platformdirs==4.1.0', 'Pygments==2.17.2', 'pywin32-ctypes==0.2.2', 'readme-renderer==42.0', 'requests==2.31.0', 'requests-toolbelt==1.0.0', 'rfc3986==2.0.0', 'rich==13.7.0', 'setuptools==69.0.3', 'twine==4.0.2', 'urllib3==2.1.0', 'userpath==1.9.1', 'wheel==0.42.0', 'zipp==3.17.0'],
    license="GNU GENERAL PUBLIC LICENSE",
    entry_points={'console_scripts': [
        "setup-generator = SetupGenerator.setupGenerator:setupGenerator"
    ]}
)
