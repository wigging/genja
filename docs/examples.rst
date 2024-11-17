Examples
========

Examples are available in the `genja <https://github.com/wigging/genja>`_ repository on GitHub. See the sections below for more information about each example.

Building the examples
---------------------

The examples are located in the **genja/examples** directory in the GitHub repository. Use the ``genja build`` or ``genja serve`` command to generate the HTML for a particular example. For instance, use the commands shown below to build the website and run a local server for the **directory-nocat** example. The example website will automatically reload in the web browser when changes are saved to the Markdown files.

.. code:: text

   cd examples/directory-nocat
   genja serve

Use the commands shown below to build the example website without starting a local server.

.. code:: text

   cd examples/directory-nocat
   genja build

Directory output with no categories
-----------------------------------

The **directory-nocat** example uses the **mysite** directory for the generated HTML output. The Markdown files are located in the **pages** and **posts** directories. The Markdown files are not organized into categories using sub-directories. The **templates** directory contains the Jinja templates.

.. code:: text

   directory-nocat/
   ├── mysite/
   │   ├── img/
   │   └── styles.css
   ├── pages/
   │   ├── about.md
   │   └── contact.md
   ├── posts/
   │   ├── apple.md
   │   └── orange.md
   ├── templates/
   │   ├── index.html
   │   ├── page.html
   │   └── post.html
   └── config.toml

Directory output with categories
--------------------------------

The **directory-withcat** example uses the **mysite** directory for the generated HTML output. The Markdown files are located in the **pages** and **posts** directories. The Markdown files are organized into categories using sub-directories. The **templates** directory contains the Jinja templates.

.. code:: text

   directory-withcat/
   ├── mysite/
   │   ├── img/
   │   └── styles.css
   ├── pages/
   │   ├── about.md
   │   └── contact.md
   ├── posts/
   │   ├── fruits/
   │   └── veggies/
   ├── templates/
   │   ├── index.html
   │   ├── page.html
   │   └── post.html
   └── config.toml

Top-level output with no categories
-----------------------------------

The **toplevel-nocat** example uses the root directory for the generated HTML output. The Markdown files are located in the **pages** and **posts** directories. The Markdown files are not organized into categories using sub-directories. The **templates** directory contains the Jinja templates.

.. code:: text

   toplevel-nocat/
   ├── img/
   │   └── apple.jpg
   ├── pages/
   │   ├── about.md
   │   └── contact.md
   ├── posts/
   │   ├── apple.md
   │   └── orange.md
   ├── templates/
   │   ├── index.html
   │   ├── page.html
   │   └── post.html
   ├── config.toml
   └── styles.css

Top-level output with no pages
------------------------------

The **toplevel-nopages** example uses the root directory for the generated HTML output. The Markdown files are located in the **posts** directory, there is no **pages** directory for this example. The Markdown files are not organized into categories using sub-directories. The **templates** directory contains the Jinja templates.

.. code:: text

   toplevel-nopages/
   ├── img/
   │   └── apple.jpg
   ├── posts/
   │   ├── apple.md
   │   └── orange.md
   ├── templates/
   │   ├── index.html
   │   └── post.html
   ├── config.toml
   └── styles.css

Top-level output with categories
--------------------------------

The **toplevel-withcat** example uses the root directory for the generated HTML output. The Markdown files are located in the **pages** and **posts** directories. The Markdown files are organized into categories using sub-directories. The **templates** directory contains the Jinja templates.

.. code:: text

   toplevel-withcat/
   ├── img/
   │   └── apple.jpg
   ├── pages/
   │   ├── about.md
   │   └── contact.md
   ├── posts/
   │   ├── fruits/
   │   └── veggies/
   ├── templates/
   │   ├── index.html
   │   ├── page.html
   │   └── post.html
   ├── config.toml
   └── styles.css
