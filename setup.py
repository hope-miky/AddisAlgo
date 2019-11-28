import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AddisAlgo",
    version="0.1",
    author="Tesfamichael Molla Ali",
    author_email="hope.miky1074@gmail.com",
    description="A Python library consisting all the basic implementation of Algorithms as a submodule. The libarary also consists all the datastructures in python and some operations that can be done on them.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tesfamichael1074/AddisAlgo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)