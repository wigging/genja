"""Function to run a local server."""

import webbrowser
from livereload import Server


def run_server(config: dict[str, str]):
    """Run a local web server.

    Run a local web server and open a browser to view the website. The website
    is automatically reloaded when changes occur in the input directory.

    Parameters
    ----------
    config
        Configuration settings from the config file.
    """
    # Get the Markdown and output directories
    output_dir = config["site_output"]

    # Open web browser to view website on localhost port
    webbrowser.open("http://localhost:5500")

    # Serve the website from the output directory and automatically reload it
    # when changes occur in the input directory
    server = Server()
    server.watch("_posts", "genja build")
    server.serve(root=output_dir)
