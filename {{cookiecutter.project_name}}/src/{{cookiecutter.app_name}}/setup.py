from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='{{cookiecutter.app_name}}',
      version=version,
      description="",
      long_description=""" """,
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "gatekeeper",
          "gk.layout",
          # -*- Extra requirements: -*-
      ],
      entry_points={
         'fanstatic.libraries': [
            '{{cookiecutter.app_name}} = {{cookiecutter.app_name}}.resources:library',
         ],
         'paste.app_factory': [
             'app = {{cookiecutter.app_name}}.utils:Application',
         ],
      }
      )
