from setuptools import setup, find_packages

setup(
    name='litholink_analysis',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'scipy',
        'openpyxl',
        'scikit-learn'
    ],
    entry_points={
        'console_scripts': [
            'litholink=main:main'
        ]
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='Analysis project for Litholink study data',
    license='MIT'
)
