# -*- coding: utf-8 -*-

import os
import sys
import json


class Configuration(object):

    def __init__(self, filename):
        if not os.path.isfile(filename):
            raise RuntimeError('Configuration file does not exist.')
        self.environ = filename
        self.backup = sys.path[:]

    def __enter__(self):
        with open(self.environ, "r") as fd:
            env = json.load(fd)

        paths = env['paths']
        sys.path[0:0] = paths
        return env['conf']

    def __exit__(self, exc_type, exc_val, exc_tb):
        # we need to make something about error handling.
        sys.path = self.backup
