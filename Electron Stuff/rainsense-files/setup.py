from setuptools import setup, find_packages

setup(
    name="RainSense",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "geopy",
        "kagglehub"
    ],
    entry_points={
        "console_scripts": [
            "rainsense = rainsense.main:run",
        ],
    },
    description="Rainwater Harvesting Estimation Tool for India",
    author="Sijo Santhosh and Shiva G",
    license="MIT",
)