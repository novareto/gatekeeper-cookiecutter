# -*- coding: utf-8 -*-

import os
from cookiecutter.main import cookiecutter


if __name__ == '__main__':
    project_path = os.path.abspath(os.path.dirname(__file__))
    cookiecutter(project_path, extra_context={'project_path': project_path})
