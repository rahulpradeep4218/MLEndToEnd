from setuptools import setup, find_packages

from typing import List
HYPHEN_E_DOT = '-e .'

def get_requirements(filepath:str) -> List[str]:
    '''
    this returns list of dependencies
    '''
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements
    

setup(
    name='ml_endtoend',
    version='0.0.1',
    author='rahul',
    author_email='rahulpradeep4218@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)