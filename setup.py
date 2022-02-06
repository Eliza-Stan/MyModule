from setuptools import setup, find_packages

setup(
    name='MyModule',
    version='0.1',
    packages=find_packages(exclude=['Test*']),
    license='MIT',
    description='EDSA make module example',
    long_description=open('ReadMe.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Eliza-Stan/PythonFiles.git',
    author='Eliza-Stan',
    author_email='elizabeth@explore-datascience.net'
)