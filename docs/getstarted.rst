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

Before running genja, create a project structure as shown below. Or create a new example project by using the ``genja new`` command. Markdown files go into the **_pages** and **_posts** directories. The **_pages** directory is for standalone content that is not dated such as an about page or contact page. The **_posts** directory is for dated content such as blog posts or articles. The **_templates** directory contains `Jinja <https://jinja.palletsprojects.com>`_ templates that are used to render the HTML pages and posts. The **mysite** directory contains the built website which can be hosted with GitHub Pages or some other web hosting platform. Lastly, the **genja.toml** defines the URLs and directories for the project.

.. code:: text

   myproject/
   ├── mysite/
   │   ├── img/
   │   └── styles.css
   ├── _pages/
   │   ├── about.md
   │   └── contact.md
   ├── _posts/
   │   ├── apple.md
   │   └── orange.md
   ├── _templates/
   │   ├── index.html
   │   ├── page.html
   │   └── post.html
   └── genja.toml

The items in the **genja.toml** are shown below. The ``base_url`` is the URL for the homepage of the website. The ``posts_output`` defines the output directory for the generated HTML posts. All of the HTML files generated from Genja are located in the ``site_output`` directory. Static content such as images and CSS files should go in this directory. The title of the website is defined by the ``title`` key.

.. code:: toml

   base_url = "https://example.com"
   posts_output = "blog"
   site_output = "mysite"
   title = "My Website"

Use the ``serve`` command to build the website and start a local server. This will automatically open the default web browser to view the website. The website will automatically reload when changes are saved to the Markdown files.

.. code:: text

   genja serve

Use the ``build`` command to build the website without running a local server.

.. code:: text

   genja build

Use the ``clean`` command to remove all the generated HTML files and the JSON feed file.

.. code:: text

   genja clean
