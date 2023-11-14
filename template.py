# This will create the folder structer for the entire project. 

import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO, format= '[%(asctime)s]: %(message)s:')

project_name = "cnnClassifier" # giving this name to make the template as genric 

list_of_files = [

    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
    
]

for filepath in list_of_files:
    # the below line of code to handle the path issues on the different operating system like windows, linux or MAC
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) # it will return the two seprate path name in tuple Data structure as return type


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating the directory:{filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating the emplty file: {filepath}")

    else:
        logging.info(f"{filename} is already exits")


