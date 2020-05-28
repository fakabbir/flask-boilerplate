import os
from setuptools import find_packages

project_directory = os.path.abspath(os.path.dirname(__file__))
about = {}

with open(os.path.join(project_directory, 'app', '__version__.py'), 'r') as f:
    exec(f.read(), about)

with open('README.md', 'r') as f:
    readme = f.read()

requires = [
    'numpy>=1.13.3',
]

cv_requires = [
    'opencv-python>=3.4.2.17'
]

plot_requires = [
    'matplotlib>=2.2.3',
]

dev_requires = [
    'codecov>=2.0.15',
    'pytest>=3.8.0',
    'pytest-cov>=2.6.0',
    'pytest-mpl>=0.10',
    'pytest-runner>=4.2',
    'Sphinx>=1.7.9'
]

all_requires = cv_requires + plot_requires
dev_requires = dev_requires + all_requires

def setup_package():
    metadata = dict(name=about['__title__'],
                    version=about['__version__'],
                    description=about['__description__'],
                    long_description=readme,
                    long_description_content_type="text/markdown",
                    url=about['__url__'],
                    author=about['__author__'],
                    author_email=about['__author_email__'],
                    license=about['__license__'],
                    packages=find_packages(exclude=('tests',)),
                    install_requires=requires,
                    extras_require={
                        'all': all_requires,
                        'cv': cv_requires,
                        'dev': dev_requires,
                        'plot': plot_requires
                    },
                    classifiers=[
                        # Trove classifiers
                        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
                        'License :: OSI Approved :: MIT License',
                        'Programming Language :: Python :: 2.7',
                        'Programming Language :: Python :: 3.5',
                        'Programming Language :: Python :: 3.6',
                        'Programming Language :: Python :: 3.7'
                    ])

    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup

    setup(**metadata)

if __name__ == '__main__':
    setup_package()