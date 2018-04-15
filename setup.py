from setuptools import setup

setup(
    name="scirate_extractor",
    description="Python wrapper for extracting content from Scirate.",
    long_description=open("README.md").read(),
    url="https://github.com/vprusso/scirate_extractor",

    author="Vincent Russo",
    author_email="vincentrusso1@gmail.com",

    packages=["scirate_extractor"],
    version="0.0.1",
    install_requires=['nose', 'bs4', 'requests'],

    license="MIT",

    keywords="scirate API",

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
    ]
)
