'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    Thiss function will return list of requirements
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Shreyash Nagrale",
    author_email="shreyashnagrale260@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)



# 🎯 Aur ab finally ek line me poora concept
# __init__.py     →   "Ye folder Python package hai."
# setup.py        →   "Is package ko install kaise karna hai?"
# pip install .   →   "Mere project ki copy Python environment me install kar do."
# pip install -e . →   "Copy mat banao, mere original project ko hi Python environment me register kar do."
# import networksecurity  →   "Python environment me registered package ko use karo."