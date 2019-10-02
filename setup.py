from setuptools import setup, find_packages

with open("README.rst") as fh_in:
    README = fh_in.read()

setup(
    name="py3odb",
    version="0.2",
    description="Python 3.6+ compatible interface to ECMWF's ODB API",
    long_description=README,
    long_description_content_type="text/x-rst",
    url="https://github.com/opus49/py3odb",
    author="Mike Puskar",
    author_email="puskar49@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.6"
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "py3odb = py3odb.cli.main:main",
        ]
    },
    project_urls={
        'Documentation': 'https://py3odb.readthedocs.io',
    }
)
