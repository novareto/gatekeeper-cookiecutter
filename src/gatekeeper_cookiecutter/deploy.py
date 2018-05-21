# -*- coding: utf-8 -*-

import os
import pkg_resources
from cookiecutter.main import cookiecutter


DATA_PATH = pkg_resources.resource_filename(
    'gatekeeper_cookiecutter', 'template/')


def generate():
    extra_context={'fullpath': os.path.abspath('.')}
    cookiecutter(DATA_PATH, extra_context=extra_context)


if __name__ == '__main__':
    generate()
