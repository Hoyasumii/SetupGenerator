from setuptools import setup

setup(
    name="hoy-setup-generator",
    version=1.2,
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
    url="https://github.com/Hoyasumii/SetupGenerator.git",
    packages=['SetupGenerator'],
    install_requires=['hoy-typed-input==1.1', 'hoyl-keyboard-manager==1.0.1', 'keyboard==0.13.5', 'python-slugify==8.0.1', 'setuptools==69.0.3', 'text-unidecode==1.3'],
    license="GPL-3.0 license",
    entry_points={'console_scripts': [
        "setup-generator = SetupGenerator.setupGenerator:setupGenerator"
    ]}
)
