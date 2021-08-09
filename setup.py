#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Marcin Morys",
    author_email='marcin.m.morys@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A Raspberry Pi hosted distance sensor to help you park perfectly in your garage, every time.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='perfectpark',
    name='perfectpark',
    packages=find_packages(include=['perfectpark', 'perfectpark.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mmorys/perfectpark',
    version='0.1.0',
    zip_safe=False,
)
