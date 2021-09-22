from setuptools import find_packages, setup

setup(
    name='Finstein',
    packages=find_packages(include=['Finstein']),
    version='1.0',
    description='A library for finacial calculations',
    author='Abhiraj Mengade',
    license='MIT',
    install_requires=['scipy'],
    setup_requires=[],
    tests_require=[],
    test_suite='Tests',
)