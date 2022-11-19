import subprocess
from importlib.metadata import version


def test_version():
    """
    Test to compare the command line version number to the installed package
    version number.
    """
    capture = subprocess.run('genja --version', shell=True, capture_output=True, text=True)
    stdout = capture.stdout
    assert stdout == version('genja') + '\n'
