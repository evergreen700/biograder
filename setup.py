import setuptools
from setuptools import setup
import os.path as path

# Get the path to our current directory
path_here = path.abspath(path.dirname(__file__))

# Get the package version from its universal storage location, biograder/version.py
version = {}
version_path = path.join(path_here, "biograder", "version.py")
with open(version_path) as fp:
    exec(fp.read(), version)

# Get the long description from the README file
readme_path = path.join(path_here, "README.md")
with open(readme_path) as readme_file:
    readme_text = readme_file.read()

setup(
    name='biograder',
    version=version['__version__'],
    author='PayneLab',
    author_email='sam_payne@byu.edu',
    description='Python packaging for biograder: automatic homework grading and hints',
    long_description=readme_text,
    long_description_content_type='text/markdown',
    url='https://github.com/PayneLab/biograder',
    packages=['biograder'],
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    zip_safe=False,
    include_package_data=True,
    project_urls={
        'Documentation': 'https://paynelab.github.io/biograder/'
    },
)
