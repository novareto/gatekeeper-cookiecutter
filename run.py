# -*- coding: utf-8 -*-

import os

from cookiecutter.main import cookiecutter

OUTPUT = "/tmp/cc/"


if __name__ == '__main__':
    project_path = os.path.abspath(os.path.dirname(__file__))
    output_path = os.path.abspath(OUTPUT)
    print "PROJECTPATH", project_path
    cookiecutter(project_path, extra_context={'project_path': project_path}, output_dir=OUTPUT)
