#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="jige003",
    author_email='jige003@x.com',
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
    description="my cookiecutter_learn github repo",
    entry_points={
        'console_scripts': [
            'my_project_slug=my_project_slug.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='my_project_slug',
    name='my_project_slug',
    packages=find_packages(include=['my_project_slug', 'my_project_slug.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jige003/my_project_slug',
    version='0.1.0',
    zip_safe=False,
)
