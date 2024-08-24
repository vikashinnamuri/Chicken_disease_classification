import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')  #used to print the loggings in the terminal 


project_name = "cnnClassifier"   #project name 

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.htm"
]


#this code is used to create rhe file and folder if there is no file in the name that we have mentioned 

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":         # condition to find the folder  is empty 
        os.makedirs(filedir, exist_ok=True)       #used to male the directory or folder 
        logging.info(f"Creating directory; {filedir} for the file: {filename}")   #print the result of the excution

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  # checking the file is exist or checkint thr file size is zero
        with open(filepath, "w") as f:   # this command is used to create and allow to write in the file  
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")