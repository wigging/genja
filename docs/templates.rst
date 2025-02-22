Templates
=========

Genja uses `Jinja templates <https://jinja.palletsprojects.com>`_ to write Markdown content to HTML files. You can probably guess where the name "Genja" came from. All template files must go in a directory named **_templates**.

Page template
-------------

The ``page.html`` template is used to render the Markdown files contained in the **_pages** directory. This template must be named ``page.html`` for Genja to recognize it. The page template is not needed if there are no pages (pages directory) for the project.

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

The ``post.html`` template is used to render the Markdown files contained in the **_posts** directory. This template must be named ``post.html`` for Genja to identify it. The post template and posts directory are required by Genja.

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
       <link rel="stylesheet" href="{% if meta.category != '_posts' %}../../{% else %}../{% endif %}styles.css">

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

The keys available in the ``meta`` dictionary are ``title``, ``date``, ``category``, ``link``, ``url``, ``iso_date``, and ``html``. The keys are defined below. Use the ``meta['title']`` or ``meta.title`` syntax to get values from the meta dictionary in the template.

title
   This is the title of the post.
date
   The long date of the post such as November 12, 2024.
category
   The category of the post. The name of the category is determined by the location of the Markdown file in the posts directory. If the post is at the top-level of the posts directory then the category is just "posts", If the post resides in a sub-directory within the posts directory, then the category is the name of the sub-directory.
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
