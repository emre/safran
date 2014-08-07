from setuptools import setup

setup(
    name='safran',
    version='0.1',
    packages=['safran'],
    url='http://github.com/emre/safran',
    license='MIT',
    author='Emre Yilmaz',
    author_email='mail@emreyilmaz.me',
    description='safran.io CLI reader',
    entry_points={
        'console_scripts': [
            'safran = safran.__main__:main',
        ],
    },
    install_requires=[
        'feedparser',
        'clint',
    ],
)