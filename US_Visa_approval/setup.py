from setuptools import setup, find_packages
# find_packages() scans the current directory and all subdirectories for Python packages.(__init__)

setup(
    name='US_Visa_Approval',
    version='0.1.0',
    description='Machine Learning model for US Visa Approval Prediction',
    author='Jeevan',
    packages=find_packages()
)