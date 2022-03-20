from setuptools import setup, find_packages

setup(
    name="github-action-tests",
    version="0.0.3",
    packages=find_packages(exclude=["tests", "tests.*"]),
    url="https://github.com/Barabazs/github-action-tests",
    license="MIT",
    author="Barabazs",
    author_email="",
    description="Test package",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)