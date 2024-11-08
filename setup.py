from distutils.core import setup
from setuptools import find_packages

setup(
    name='labjackt7',
    version='0.1',
    description='High-level Labjack T7 interface, warapping LJM Python library for data acquisition and waveform or pattern generation',
    author='Jeremiah Heilman',
    author_email='jeremiah.heilman@gmail.com',
    packages=find_packages(),
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=['labjack-ljm', 'numpy', 'StrEnum']
)
