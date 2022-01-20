"""Package setup"""
from setuptools import setup, find_packages


with open("playful/version.py", "r", encoding="utf-8") as version:
    __version__ = ""
    exec(version.read(), globals())  # pylint: disable=exec-used


with open("README.md", "r", encoding="utf-8") as readme:
    README = readme.read()


setup(
    name="playful",
    version=__version__,
    description="A Python package that implements classic computer and board games.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jason-ash/playful",
    author="Jason Ash",
    author_email="ash.jasont@gmail.com",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        "dev": [
            "black==21.7b0",
            "codespell==2.1.0",
            "pre-commit==2.13.0",
            "pylint==2.9.6",
            "mypy==0.910",
        ]
    },
    include_package_data=True,
    package_data={"playful": ["../README.md", "../LICENSE.md"]},
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    test_suite="tests",
    zip_safe=False,
)
