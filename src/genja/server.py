"""
Function to run a server.
"""

import webbrowser
from livereload import Server


def run_server(config):
    """
    Run a local web server.

    Run a local web server and open a browser to view the website. The website
    is automatically reloaded when changes occur in the input directory.

    Parameters
    ----------
    config : dict
        Configuration dictionary that contains `base_url`, `input_dir`, and
        `output_dir` keys.
    """

    # Get the input and output directories
    input_dir = config["input_dir"]
    output_dir = config["output_dir"]

    # Open web browser to view website on localhost port
    webbrowser.open("http://localhost:5500")

    # Serve the website from the output directory and automatically reload it
    # when changes occur in the input directory
    server = Server()
    server.watch(input_dir, "genja build")
    server.serve(root=output_dir)
