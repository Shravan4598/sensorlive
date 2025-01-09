from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
    requirements_list:List[str]=[]
    return requirements_list

    
setup(
    name="sensor",
    version="0.0.1",
    author="Shravan",
    author_email="shravankumarpandey825412@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),    #["pymongo"]
)