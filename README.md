Blog built with Django
=============

Responsive blog web app built with [Django](https://www.djangoproject.com/) and [PostgreSQL](http://www.postgresql.org/).

Through the Django admin interface, the user can create blog entries, which include commenting functionality from [Disqus](https://disqus.com/). 


Configuration
------------
Configuring this project should be consistent across Mac (local) and Vagrant.  You should already have [Python 2](https://www.python.org/) installed before cloning.

Start by cloning the repository
```
$ git clone https://github.com/carmenvkrol/django-blog.git
```

Once that's complete, install the remaining dependencies by running
```
$ pip install
```

Running the Application
------------
To run the application locally, run the following in the terminal:

```
$ python blog/manage.py runserver
```

The application runs on port 8000.


Directory Structure
------------
```
django-blog/
 |__blog/
 |  |__blog/ #server-side settings files
 |  |__cvk-blog/ #server-side files for database modals and routing as well as client-side files
 |  |  |__migrations/
 |  |  |__static/ #client-side files including styles and images
 |  |  |__templates/ #html templates for client-side rendering
```

Python Packages
------------
A list of other plugins used in this application and their purpose:

**[AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html#install-with-pip)** - command line interface tool for Amazon Web Services (AWS), if you decide to deploy blog with AWS.

**[bcdoc](https://pypi.python.org/pypi/bcdoc/0.16.0)** - helps document botocore-based projects.

**[botocore](https://github.com/boto/botocore)** - foundation for AWS CLI (see above in this section).

**[colorama](https://pypi.python.org/pypi/colorama)** - color terminal text.

**[cssselect](https://pypi.python.org/pypi/cssselect/0.9.1)** - parses CSS3 selectors and translates into XPath 1.0 expressions, useful for html templating.

**[cssutils](https://pypi.python.org/pypi/cssutils/1.0)** - parse and build CSS stylesheets.

**[dj-database-url](https://pypi.python.org/pypi/dj-database-url/0.3.0)** - use database urls in Django application.

**[dj-static](https://pypi.python.org/pypi/dj-static/0.0.6)** - serve production static files with Django

**[Django](https://pypi.python.org/pypi/Django/1.8.4)** - Python framework upon which this repo is built.

**[django-disqus](https://pypi.python.org/pypi/django-disqus/0.5)** - use disqus with Django, specifically in blog entries.

**[django-markdown-deux](https://pypi.python.org/pypi/django-markdown-deux/1.0.5)** - use markdown in Django blog entries.

**[django-toolbelt](https://pypi.python.org/pypi/django-toolbelt/0.0.1)** - collection of common Django utilities.

**[docopt](https://pypi.python.org/pypi/docopt/0.6.2)** - Python argument parser.

**[docutils](https://pypi.python.org/pypi/docutils/0.12)** - modular system for processing documentation into formats such as HTML and XML.

**[funcsigs](https://pypi.python.org/pypi/funcsigs/0.4)** - Python function signatures.

**[gunicorn](https://pypi.python.org/pypi/gunicorn/19.3.0)** - WSGI HTTP server for UNIX.

**[Jinja2](https://pypi.python.org/pypi/Jinja2/2.8)** - template engine for Python.

**[jmespath](https://pypi.python.org/pypi/jmespath/0.7.1)** - allow declaratively specify how to extract elements from JSON.

**[lxml](https://pypi.python.org/pypi/lxml/3.4.4)** - Pythonic XML processing library.

**[mandrill](https://pypi.python.org/pypi/mandrill/1.0.57)** - CLI client and Python API library for Mandrill email as a service platform.

**[markdown2](https://pypi.python.org/pypi/markdown2/2.3.0)** - allows using Markdown with Python.

**[MarkupSafe](https://pypi.python.org/pypi/MarkupSafe/0.23)** - Implements a XML/HTML/XHTML Markup safe string for Python.

**[mock](https://pypi.python.org/pypi/mock/1.3.0)** - Python test library.

**[pbr](https://pypi.python.org/pypi/pbr/1.7.0)** - library that injects some default tools into setuptools run.

**[premailer](https://pypi.python.org/pypi/premailer/2.9.5)** - turns external CSS styles into inline styles.  Useful for html emails.

**[psycopg2](https://pypi.python.org/pypi/psycopg2/2.6.1)** - Python-PostgreSQL database adapter.

**[pyasn1](https://pypi.python.org/pypi/pyasn1/0.1.8)** - implementation of ASN.1 types and codecs in Python.

**[python-dateutil](https://pypi.python.org/pypi/python-dateutil/2.4.2)** - extensions for standard Python datetime module.

**[requests](https://pypi.python.org/pypi/requests/2.7.0)** - simplifies HTTP requests.

**[rsa](https://pypi.python.org/pypi/rsa/3.2)** - Python RSA implementation that supports encryption, including authorization.

**[six](https://pypi.python.org/pypi/six/1.9.0)** - compatibility library for Python 2 and Python 3.

**[static3](https://pypi.python.org/pypi/static3/0.6.1)** - WSGI library for serving static content.

**[virtualenv](https://pypi.python.org/pypi/virtualenv/13.1.2)** - virtual environment builder for Python.