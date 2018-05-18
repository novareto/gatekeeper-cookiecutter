# -*- coding: utf-8 -*-

import os
from cookiecutter.main import cookiecutter


def main():
    project_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'template')
    extra_context={'fullpath': os.path.abspath('.')}
    cookiecutter(project_path, extra_context=extra_context)


if __name__ == '__main__':
    main()
