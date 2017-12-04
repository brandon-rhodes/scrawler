import os
from distutils.core import setup

README_PATH = os.path.join(os.path.dirname(__file__), 'scrawler', '__init__.py')
with open(README_PATH, encoding="utf-8") as f:
    README_TEXT = f.read()

setup(
    name='scrawler',
    version='1.0',
    description='ASCII art animation framework for my North Bay Python talk',
    long_description=README_TEXT,
    author='Brandon Rhodes',
    author_email='brandon@rhodesmill.org',
    url='https://github.com/brandon-rhodes/scrawler',
    packages=['scrawler', 'adventure/tests'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Games/Entertainment',
        ],
    )
