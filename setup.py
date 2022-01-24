from setuptools import setup

with open("README.md", 'r') as fh:
    long_description = fh.read()

setup(
    name='dor-utils',
    version='0.0.1',
    description='Some utils by Dor Miron',
    py_modules=[],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU General Public"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",

    install_requires=[
        "numpy~=1.22.1",
        "matplotlib~=3.5.1"
    ]

    # url=""
)
