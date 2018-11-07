#!/usr/bin/env python
from client.core import handler

import os, sys

BASE_DIR = os.path.dirname(os.getcwd())

sys.path.append(BASE_DIR)

if __name__ == '__main__':
    handler.ArgvHandler(sys.argv)

