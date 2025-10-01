Templates
=========

Genja uses `Jinja templates <https://jinja.palletsprojects.com>`_ to write Markdown content to HTML files. You can probably guess where the name "Genja" came from. All template files must go in a directory named ``_templates``.

Page template
-------------

The ``page.html`` template is used to render the Markdown files contained in the ``_pages`` directory. This template must be named ``page.html`` for Genja to recognize it. The page template is not needed if there are no pages (pages directory) for the project.

An example of a page template is given below. The ``{{ content }}`` is where the content of the Markdown file is rendered. Unlike the post template discussed in the next section, the Markdown content is the only data provided to the page template.

.. code:: html

   <!DOCTYPE html>
   <html>
   <head>
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1">

       <!-- Bootstrap -->
       <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet">

       <!-- Styles -->
       <link rel="stylesheet" href="styles.css">

       <title>My Website</title>
   </head>
   <body>
   <div class="container">
       <div class="row">
           <div class="col-md">

               {{ content }}

           </div>
       </div>
   </div>
   </body>
   </html>

Post template
-------------

The ``post.html`` template is used to render the Markdown files contained in the ``_posts`` directory. This template must be named ``post.html`` for Genja to identify it. The post template and posts directory are required by Genja.

An example of a post template is given below. The ``{{ content }}`` variable is where the content of the Markdown file is rendered. A ``meta`` dictionary that contains information about the post is also available in the template.

.. code:: html

   <!DOCTYPE html>
   <html>
   <head>
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1">

       <!-- Open Graph -->
       <meta property="og:url" content="{{ meta.url }}">
       <meta property="og:type" content="website">
       <meta property="og:title" content="My Website">
       <meta property="og:description" content="Description for my website.">
       <meta property="og:image" content="https://example.com/img/apple.jpg">

       <!-- Bootstrap -->
       <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">

       <!-- Styles -->
       <link rel="stylesheet" href="../styles.css">

       <title>My Website</title>
   </head>
   <body>
   <div class="container">
       <div class="row">
           <div class="col-md">

               <h2 class="mt-4">{{ meta.title }}</h2>

               <h6>Written on {{ meta.date }}</h6>

               {{ content }}

           </div>
       </div>
   </div>
   </body>
   </html>

The keys available in the ``meta`` dictionary are ``title``, ``date``, ``categories``, ``tags``, ``link``, ``url``, ``iso_date``, and ``html``. The keys are defined below. Use the ``meta['title']`` or ``meta.title`` syntax to get values from the metadata dictionary in the template.

title
   This is the title of the post defined in Markdown as ``title: The post title`` and is returned as a string in the template.
date
   The long date of the post such as ``date: November 12, 2024`` returned as a string in the template.
categories
   The category or categories of the post as a list of strings. A single category defined in the Markdown as ``categories: fruit`` is a returned in the template as a list containing one string value. Multiple categories such as ``categories: fruit, veggie`` are returned as a list of several string values. Notice that each category must be separated by a comma followed by a space.
tags
   The tag or tags of the post as a list of strings. This can be a single tag defined as ``tags: python`` or multiple tags defined as ``tags: python, swift``. Each tag must be separated by a comma followed by a space.
link
   The relative link to the post's generated HTML file.
url
   The full URL to the post's generated HTML file. This uses the ``base_url`` from the Genja config file. This is the full link to the HTML post.
iso_date
   The ISO date of the post.
html
   The HTML snippet used for the JSON feed. This is not needed for the post template.

Base template
-------------

A ``base.html`` template can be used as a skeleton document for the other HTML templates. See the `Jinja documentation <https://jinja.palletsprojects.com/en/stable/templates/#template-inheritance>`_ for more information about using base templates.
