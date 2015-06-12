# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from os.path import abspath, dirname

import nose


def all():
    argv = ['nosetests', '--verbose', '--logging-level=ERROR']
    nose.run_exit(argv=argv, defaultTest=abspath(dirname(__file__)))

if __name__ == '__main__':
    all()
