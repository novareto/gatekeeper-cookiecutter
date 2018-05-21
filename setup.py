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
      include_package_data=True,
      zip_safe=False,
      packages=find_packages('src'),
      package_dir={'': 'src'},
      package_data={
        'gatekeeper_cookiecutter': ['template'],
      },
      install_requires=[
          "wheel",
          "cookiecutter",
      ],
      entry_points = {
          'console_scripts': [
              'generate=gatekeeper_cookiecutter.deploy:generate'
          ],
      }
)
