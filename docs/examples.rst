Examples
========

Examples are available on `GitHub <https://github.com/wigging/genja>`_ in the Genja repository. See the sections below for more information about each example.

Directory website
-----------------

The ``directory-website`` example uses the ``website`` directory for the generated output. The ``_mdcontent`` directory contains the Markdown files used by Genja to generate the HTML files. The ``_templates`` directory contains the Jinja2 templates.

Use the commands shown below to build the website and run a local server to view the website in the default web browser. The website will automatically reload in the web browser when changes are saved to the Markdown files.

.. code:: text

   cd examples/directory-website
   genja serve

Use the commands shown below to build the example website without starting a local server.

.. code:: text

   cd examples/directory-website
   genja build

Top-level output
----------------

The ``toplevel-output`` example uses the top-level directory for the generated output. The ``_notes`` directory contains the Markdown files used by Genja to generate the HTML files. The ``_templates`` directory contains the Jinja2 templates.

Use the commands shown below to build the website and run a local server to view the website in the default web browser. The website will automatically reload in the web browser when changes are saved to the Markdown files.

.. code:: text

   cd examples/toplevel-output
   genja serve

Use the commands shown below to build the example website without starting a local server.

.. code:: text

   cd examples/toplevel-output
   genja build
