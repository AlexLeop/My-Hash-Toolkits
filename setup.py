""" Setup do Pacote Kit_Hash"""
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Kit_Hash",
    version="0.0.1",
    author="Alex Leopoldo",
    author_email="lx.leopoldo@outlook.com",
    description="Ferramenta para gerar e comparar diferentes hashes",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.9',
)
