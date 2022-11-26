from setuptools import setup, find_packages

long_description = open('./README.md')

setup(
    name='ASTormtrooper',
    version='2.1.1',
    url='https://github.com/ZSendokame/ASTormTrooper',
    license='MIT license',
    author='ZSendokame',
    description='Lint your code with lambdas.',
    long_description=long_description.read(),
    long_description_content_type='text/markdown',

    packages=(find_packages(include=['astt']))
)