from setuptools import setup, find_packages

setup(
    name='simplePyCLI',
    version='1',
    author='Aleksandr Chasnyk',
    author_email='alexandr.chasnyk@yandex.com',
    description='Simple CLI for micropython and python projects when command line interface is required.',
    packages=find_packages(),  # Automatically find packages to include
    url='https://github.com/ami3go/simplePyCLI',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
            ],
    )

