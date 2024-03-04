import os
from pathlib import Path
import logging

#logging string is used instead of print statement

# log level name is specified(infor related log), format of the log is specified--ascii time
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'KidneyDiseaseClassification'  #project name

list_of_files = [
    ".github/workflows/.gitkeep", #when we create cicd pipeline then we remove gitkeep...gitkeep make this file to not get uploaded
    f"src/{project_name}/__init__.py", #src folder
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py", #utility files
    f"src/{project_name}/config/__init__.py"
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/enitity/__init__.py",
    f"src/{project_name}/constants/__init.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    "templates/index.html"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creatinng directory; {filedir} for the file: {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")
