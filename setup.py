from setuptools import setup

setup(
    name="scirate",
    description="Python wrapper for extracting content from Scirate.",
    long_description=open("README.rst").read(),
    url="https://github.com/vprusso/scirate",

    author="Vincent Russo",
    author_email="vincentrusso1@gmail.com",

    packages=["scirate"],
    version="0.0.2",
    install_requires=['nose', 'bs4', 'lxml', 'requests'],

    license="MIT",

    keywords=["scirate", "scirate API", "scirate python"],

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
    ],

    project_urls={
        "Homepage": "http://vprusso.github.io/",
    }
)
