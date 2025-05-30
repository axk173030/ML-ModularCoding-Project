from setuptools import setup,find_packages
from typing import List

PROJECT_NAME = "my_packageMachine Learning"
VERSION= "0.0.1"
DESCRIPTION="this is machine learning project modular coding"
AUTHOR="Shivam "
AUTHOR_EMAIL = "dummy@gmail.com"

REQUIREMENTS_FILE_NAME="requirements.txt"

HYPHEN_E_DOT="-e ."

def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list= requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n"," ")for requirement_name in requirement_list]
        

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=get_requirements_list()
)
