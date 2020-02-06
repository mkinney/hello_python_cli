import subprocess
import re


def test_version():
    rc, out = subprocess.getstatusoutput('python main.py --version')
    assert out == '0.0.1'
    assert re.match(r'[0-9]+\.[0-9]+\.[0-9]', out)
    assert rc == 0


def test_help():
    rc, out = subprocess.getstatusoutput('python main.py --help')
    assert re.match('Usage', out)
    assert rc == 0


def test_noname():
    rc, out = subprocess.getstatusoutput('python main.py')
    assert rc == 0
    assert out == 'Hello world'
