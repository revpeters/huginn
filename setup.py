from setuptools import setup

setup(
    name='Huginn',
    version='1.0',
    py_modules=['huginn'],
    install_requires=[
        'Click',
        'pytz',
    ],
    entry_points='''
    [console_scripts]
    huginn=huginn:cli
  ''',
)