from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = 'This library enables the generation of up to 5000 random user data using the RandomUser API and stores it.'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / 'README.md').read_text()

# Setting up
setup(
    name="randusergen",
    version=VERSION,
    author="codewithwan",
    author_email="<deezerxstore@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/codewithwan/randusergen',
    packages=find_packages(),
    license='MIT',
    install_requires=[],
    keywords=['random', 'user', 'generator'],
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)
