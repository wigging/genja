Example
=======

A full example is available on `GitHub <https://github.com/wigging/genja>`_ in the Genja repository.

To run the example, go to the **example** directory in the repository. The **mdcontent** folder is the input directory containing the Mardkown files. The **website** folder is the output directory containing the built HTML files. Use the commands shown below to build the website and run a local server to view the website in the default web browser. The website will automatically reload in the web browser when changes are saved to the Markdown files.

.. code:: text

   cd example
   genja serve

Use the commands shown below to build the example website without starting a local server.

.. code:: text

   cd example
   genja build
