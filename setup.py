# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='service-identity',
    version='24.2.0',
    description='Service identity verification for pyOpenSSL & cryptography.',
    author_email='Hynek Schlawack <hs@ox.cx>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed',
    ],
    install_requires=[
        'attrs>=19.1.0',
        'cryptography',
        'pyasn1',
        'pyasn1-modules',
    ],
    extras_require={
        'dev': [
            'coverage[toml]>=5.0.2',
            'idna',
            'mypy',
            'pyopenssl',
            'pytest',
            'types-pyopenssl',
        ],
        'docs': [
            'furo',
            'myst-parser',
            'pyopenssl',
            'sphinx',
            'sphinx-notfound-page',
        ],
        'idna': [
            'idna',
        ],
        'mypy': [
            'idna',
            'mypy',
            'types-pyopenssl',
        ],
        'tests': [
            'coverage[toml]>=5.0.2',
            'pytest',
        ],
    },
    packages=[
        'service_identity',
    ],
    package_dir={'': 'src'},
)
