import os
import pytest

from docopt import docopt

def test_version():
    exit_status = os.system('python main.py --version')
    assert exit_status == 0

def test_help():
    exit_status = os.system('python main.py --help')
    assert exit_status == 0

def test_noname():
    exit_status = os.system('python main.py')
    assert exit_status == 0
