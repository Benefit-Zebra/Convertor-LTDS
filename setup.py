from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="Convertor-LTDS",
    version="0.1.4",
    description="A Python package to convert between Lists,Tuples,Dictionaries and Sets.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Benefit-Zebra/Convertor-LTDS",
    author="Benefit Zebra",
    author_email="benefitzebra4707@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["convert_ltds"],
    include_package_data=True,
    project_urls={
            "Source": "https://github.com/Benefit-Zebra/Convertor-LTDS",
            "Bug Reports": "https://github.com/Benefit-Zebra/Convertor-LTDS/issues",
        }
)
