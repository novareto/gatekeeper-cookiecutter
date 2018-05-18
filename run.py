# -*- coding: utf-8 -*-

import os

from cookiecutter.main import cookiecutter

if __name__ == '__main__':
    project_path = os.path.abspath(os.path.dirname(__file__)) + '/gatekeeper-cookiecutter'

    extra_context={'fullpath': os.path.abspath('.')}
    cookiecutter(project_path, extra_context=extra_context)
