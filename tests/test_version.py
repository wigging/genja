"""
Tests for version number.
"""

import subprocess
from importlib.metadata import version


def test_version():
    """
    Test the version number.

    Compare the command line version number to the installed package version
    number. Both should give the same version number.
    """
    capture = subprocess.run("genja --version", shell=True, capture_output=True, text=True)
    stdout = capture.stdout
    assert stdout == version("genja") + "\n"
