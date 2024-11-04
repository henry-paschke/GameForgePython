# setup.py

from setuptools import setup, find_packages

setup(
    name='gameforge',
    version='1.0',
    packages=find_packages(),
    install_requires=[],
    description='Game development utility classes',
    author='Henry Paschke',
    author_email='h3nry.pas@gmail.com',
    url='https://github.com/henry-paschke/GameForgePython',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)