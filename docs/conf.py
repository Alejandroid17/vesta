# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

import django
from recommonmark.parser import CommonMarkParser

django_version = ".".join(map(str, django.VERSION[0:2]))
python_version = ".".join(map(str, sys.version_info[0:2]))

sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'vesta.settings.base'
django.setup()

# -- Project information -----------------------------------------------------

project = 'Vesta'
copyright = '2020, Alejandro'
author = 'Alejandro'

# The full version, including alpha/beta/rc tags
release = '0'

# Auto-generate API documentation.
os.environ['SPHINX_APIDOC_OPTIONS'] = "members,show-inheritance"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.apidoc',
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_parsers = {
    '.md': CommonMarkParser,
}

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**/*.migrations.rst']

# -- Options for HTML output -------------------------------------------------

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'prev_next_buttons_location': 'both',
    'collapse_navigation': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# -- Extension configuration -------------------------------------------------

autodoc_member_order = 'bysource'
autodoc_inherit_docstrings = False

apidoc_module_dir = '../../vesta'
apidoc_output_dir = 'source'
apidoc_excluded_paths = [
    '**/migrations',
    'manage.py',
    'vesta/wsgi.py',
    'vesta/asgi.py',
    'vesta/settings/local.py',
    '**/urls.py',
]
apidoc_separate_modules = True
apidoc_toc_file = False
apidoc_module_first = True
apidoc_extra_args = ['-f']

# -- Options for intersphinx extension ---------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/{}'.format(python_version), None),
    'django': ('https://docs.djangoproject.com/en/{}/'.format(django_version),
               'https://docs.djangoproject.com/en/{}/_objects/'.format(django_version)),
    'djangorestframework-jsonapi': ('https://django-rest-framework-json-api.readthedocs.io/en/stable/',
                                    'https://django-rest-framework-json-api.readthedocs.io/en/stable/objects.inv'),
    # DRF doesn't use sphinx but rather mkdocs:-(
    # 'djangorestframework': ('https://django-rest-framework.readthedocs.io/en/stable/', None),
}
