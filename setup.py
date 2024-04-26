from setuptools import setup, find_packages

setup(
    name='simplePyCLI',
    version='1.0',
    author='Aleksandr Chasnyk',
    author_email='alexandr.chasnyk@yandex.com',
    description='Simple CLI for micropython and python projects when command line interface is required.',
    packages=find_packages(),  # Automatically find packages to include
    url='https://github.com/ami3go/simplePyCLI',
    classifiers=[
            'Development Status :: 1.0',
            'License :: OSI Approved :: GNU General Public License v3.0',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
    ],

    # install_requires=[
    #     # List dependencies required by your package
    #     '',
    # ],
    # entry_points={
    #     'console_scripts': [
    #         # Define any command-line scripts provided by your package
    #         'your_script_name = your_package.module:main_function',
    #     ],
    # },
    # Other metadata (author, description, etc.)
)