from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='gatekeeper_cookiecutter',
      version=version,
      description="",
      long_description=""" """,
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      package_dir = {'': '.'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "cookiecutter",
      ],
      entry_points = {
          'console_scripts': ['gatekeeper-cookiecutter=deploy:main'],
      }
)
