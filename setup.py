"""sfdclib package setup"""

import textwrap
from setuptools import setup

setup(
    name='sfdclib',
    version='0.2.6',
    author='Andrey Shevtsov',
    author_email='ashevtsov@rbauction.com',
    packages=['sfdclib'],
    url='https://github.com/rbauction/sfdclib',
    license='MIT',
    description=("SFDClib is a Salesforce.com Metadata API and Tooling "
                 "API client built for Python 3.3 and 3.4."),
    long_description=textwrap.dedent(open('README.rst', 'r').read()),
    package_data={'': ['LICENSE']},
    package_dir={'sfdclib': 'sfdclib'},
    install_requires=[
        'requests[security]'
    ],
    keywords="python salesforce salesforce.com metadata tooling api",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ]
)
