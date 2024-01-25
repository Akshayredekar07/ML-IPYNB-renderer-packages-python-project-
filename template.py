import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s"
)

while True:
    project_name=input("Enter the project name: ")
    if project_name != '':
        break

logging.info(f"Creating Project by name: {project_name}")


"""Python Packaging project

Keyword arguments:
argument -- description
Return: return_description

packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── src/
│   └── example_package_YOUR_USERNAME_HERE/
│       ├── __init__.py
│       └── example.py
└── tests/
"""

## list of files
list_of_files = [
    ".github/workflows/.gitkeep", #.gitkeep dummy file
    f"src/{project_name}/__init__.py", #src contains all scripts
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh", #help to create basic conda env setup
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at : {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating the newfile: {filename} at path {filepath}")
    else:
        logging.info(f"file already present at: {filepath}")
                                 