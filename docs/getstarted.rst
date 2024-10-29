Getting started
===============

Genja is distributed on `PyPI <https://pypi.org/project/genja/>`_. Instructions for installing and using Genja are given below.

Installation
------------

Download and install Python from https://www.python.org or from Anaconda at https://www.anaconda.com. After installing Python, create and activate a virtual environment as shown below:

.. code:: text

   python -m venv .venv
   source .venv/bin/activate

Install the Genja package in your Python environment using pip:

.. code:: text

   pip install genja

Check the installed version from the command line:

.. code:: text

   genja --version

Usage
-----

Before running genja, create a project structure as shown below. The **content** directory contains Markdown files that are used to generate HTML files. The **templates** directory contains `Jinja <https://jinja.palletsprojects.com>`_ templates that are used to render the HTML pages. The **docs** directory contains the built website which can be hosted with GitHub Pages. Lastly, the **config.toml** defines the URLs and directories for the project.

.. code:: text

   myproject/
   ├── content/
   ├── templates/
   ├── docs/
   └── config.toml

The items in the **config.toml** are shown below. The ``base_url`` is the URL for the homepage of the website. Markdown files that are parsed by Genja are located in the ``markdown_dir`` directory. The Jinja2 templates used by Genja are located in the ``template_dir`` directory The HTML files generated from Genja are located in the ``output_dir`` directory. Static content such as images and CSS files should go in the output directory.

.. code:: toml

   base_url = "https://example.com/mywebsite"
   markdown_dir = "content"
   template_dir = "templates"
   output_dir = "docs"

Use the ``serve`` command to build the website and start a local server. This will automatically open the default web browser to view the website. The website will automatically reload when changes are saved to the Markdown files.

.. code:: text

   genja serve

Use the ``build`` command to build the website without running a local server.

.. code:: text

   genja build
