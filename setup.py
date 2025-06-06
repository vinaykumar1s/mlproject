from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    this function will return list of requirements
    '''
    requirement_list:List[str]=[]
    try:
        with open('requirement.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            #process each file
            for line in lines:
                requirement=line.strip()
                #ignore empty lines after installing packages from requirements and -e.
                if requirement and requirement!='-e.':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requriment.txt file not found")
    return requirement_list
print(get_requirements())
            

setup(
    name="mlprojects",
    version="0.0.1",
    author="vinaykumar1s",
    author_email="vinaykumar.45569@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)