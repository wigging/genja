import subprocess


def test_inputs():
    """
    Test for error if no inputs are given.
    """
    capture = subprocess.run('genja', shell=True, capture_output=True)
    returncode = capture.returncode
    assert returncode == 2
