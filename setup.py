from setuptools import setup

import re

# extract version from __init__.py
with open('html5validator/__init__.py', 'r') as f:
    INIT = f.read()
    VERSION = re.finditer('__version__ = \"(.*?)\"', INIT).next().group(1)

setup(
    name='html5validator',
    version=VERSION,
    packages=['html5validator', 'scripts'],
    license='LICENSE',
    description='Validate HTML5 files.',
    long_description=open('README.md').read(),
    author='Sven Kreiss',
    author_email='me@svenkreiss.com',

    data_files=[('', ['vnu/vnu.jar'])],
    include_package_data=True,

    install_requires=[
        '',
    ],

    entry_points={
        'console_scripts': [
            'html5validator = scripts.validate:main',
        ]
    }
)
