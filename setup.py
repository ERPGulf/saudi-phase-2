from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in saudi_einvoice/__init__.py
from saudi_einvoice import __version__ as version

setup(
	name="saudi_einvoice",
	version=version,
	description="Implementation of saudi_einvoice",
	author="erpgulf.com",
	author_email="support@erpgulf.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
