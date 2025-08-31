Examples
========

Examples are available in the ``genja/examples`` directory in the genja `GitHub <https://github.com/wigging/genja>`_ repository. Use the ``genja build`` or ``genja serve`` command to generate the HTML for a particular example. For instance, use the command shown below to build the website and run a local server for the ``directory-output`` example. The website will automatically reload in the web browser when changes are saved to the Markdown files.

.. code:: text

   cd examples/directory-output
   genja serve

Alternatively, use the build command to build the website without starting a local server.

.. code:: text

   cd examples/directory-output
   genja build

Code blocks
-----------

The ``code-blocks`` example demonstrates the use of `highlight.js <https://highlightjs.org>`_ to provide syntax coloring of code that is rendered in pages and posts. The CSS and JavaScript for hightlightjs must be defined in the ``<head>...</head>`` section in the HTML page or post template such as:

.. code:: html

   <!-- Highlightjs -->
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/styles/github-dark.min.css">
   <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/highlight.min.js"></script>
   <script>hljs.highlightAll();</script>

Next, code blocks can be defined in the Markdown files as follows:

.. code:: text

   ```python
   def seyhello():
       s = "hello there"
       print(s)
   ```

Directory output
----------------

The ``directory-output`` example defines ``site_output = "mysite"`` in the ``genja.toml`` file. This tells Genja to output the generated content to the ``mysite`` directory in the project.

.. code:: text

   directory-output/
   ├── _pages/
   ├── _posts/
   ├── _templates/
   ├── mysite/      <-- output from Genja will go in this directory
   └── genja.toml

HTML content
------------

The ``html-content`` example demonstrates putting HTML in the Markdown file.

Image files
-----------

The ``image-files`` example shows how to embed images in the Markdown file.

Pages and posts
---------------

The ``pages-and-posts`` examples demonstrates creating pages and posts as Markdown files.

Root output
-----------

The ``root-output`` example generates the HTML website content at the root level of the project.

Sort posts
----------

The ``sort-posts`` example sorts the posts.

