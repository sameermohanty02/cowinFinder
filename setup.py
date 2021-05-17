from setuptools import setup, find_packages

install_requires = [
    'Click',
    'pyyaml',
    'requests',
    'pandas',
    'beepy'
    ]

setup(
    name='cowin',
    version='1.0.0',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points='''
        [console_scripts]
        cowin=cli.main:main
    ''',
)
