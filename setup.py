from setuptools import setup, find_packages

setup(
    name='vdatetime',
    version='0.0.1',
    author='Luffy51k',
    author_email="luffy51k@gmail.com",
    long_description="my datetime utils",
    install_requires=[
        'wheel',
        'pytz'
    ],
    packages=find_packages(),
)