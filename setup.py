from setuptools import find_packages, setup


setup(
    name="cambiare",
    packages=find_packages(include=["cambiare"]),
    version="0.1.0",
    description="A lightweight music format conversion library",
    author="Dhruv Ranjan",
    license="MIT",
    install_requires=["music21", "pillow"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==6.2.5"],
    test_suite="tests"
)
