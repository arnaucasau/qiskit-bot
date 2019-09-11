# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2019
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import os

import fixtures


class FakeMetaRepo(fixtures.Fixture):

    def __init__(self, tempdir, old_meta_version, terra_version='0.9.0',
                 aer_version='0.3.0', ibmq_version='0.3.2',
                 ignis_version='0.2.0', aqua_version='0.6.0'):
        super(FakeMetaRepo, self).__init__()
        self.tempdir = tempdir
        self.terra_version = terra_version
        self.aer_version = aer_version
        self.ibmq_version = ibmq_version
        self.ignis_version = ignis_version
        self.aqua_version = aqua_version
        self.old_meta_version = old_meta_version

    def setUp(self):
        super(FakeMetaRepo, self).setUp()
        setup_py_str = """
from setuptools import setup

requirements = [
    "qiskit-terra==%s",
    "qiskit-aer==%s",
    "qiskit-ibmq-provider==%s",
    "qiskit-ignis==%s",
    "qiskit-aqua==%s",
]

setup(
    name="qiskit",
    version="%s",
    description="Software for developing quantum computing programs",
    long_description="Qiskit is a software development kit for writing "
                     "quantum computing experiments, programs, and "
                     "applications. Works with Python 3.5, 3.6, and 3.7",
    url="https://github.com/Qiskit/qiskit",
    author="Qiskit Development Team",
    author_email="qiskit@us.ibm.com",
    license="Apache 2.0",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
    ],
    keywords="qiskit sdk quantum",
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.5",
)
        """ % (self.terra_version, self.aer_version, self.ibmq_version,
               self.ignis_version, self.aqua_version, self.old_meta_version)

        with open(os.path.join(self.tempdir.path, 'setup.py'), 'w') as fd:
            fd.write(setup_py_str)

        os.mkdir(os.path.join(self.tempdir.path, 'docs'))
        docs_conf_str = """
# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Qiskit'
copyright = '2019, Qiskit Development Team'
author = 'Qiskit Development Team'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = '%s'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',
    'sphinx_tabs.tabs',
    'sphinx_automodapi.automodapi',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['theme/_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# If true, figures, tables and code-blocks are automatically numbered if they
# have a caption.
numfig = True

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# For Adding Locale
locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# A boolean that decides whether module names are prepended to all object names
# (for object types where a “module” of some kind is defined), e.g. for
# py:function directives.
add_module_names = False

# A list of prefixes that are ignored for sorting the Python module index
# (e.g., if this is set to ['foo.'], then foo.bar is shown under B, not F).
# This can be handy if you document a project that consists of a single
# package. Works only for the HTML builder currently.
modindex_common_prefix = ['qiskit.']

# -- Configuration for extlinks extension ------------------------------------
# Refer to https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_materialdesign_theme' # use the theme in subdir 'theme'

html_sidebars = {
   '**': ['globaltoc.html']
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    # Specify a list of menu in Header.
    # Tuples forms:
    #
    # Third argument:
    # True indicates an external link.
    # False indicates path of pages in the document.
    #
    # Fourth argument:
    # Specify the icon name.
    # For details see link.
    # https://material.io/icons/
    'header_links': [],

    # Customize css colors.
    # For details see link.
    # https://getmdl.io/customize/index.html
    #
    'primary_color': 'blue',
    # Values: Same as primary_color. (Default: pink)
    'accent_color': 'indigo',

    # Customize layout.
    # For details see link.
    # https://getmdl.io/components/index.html#layout-section
    'fixed_drawer': True,
    'fixed_header': False,
    'header_waterfall': True,
    'header_scroll': False,

    # Render title in header.
    # Values: True, False (Default: False)
    'show_header_title': False,
    # Render title in drawer.
    # Values: True, False (Default: True)
    'show_drawer_title': True,
    # Render footer.
    'show_footer': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['theme/static/']

html_favicon = 'theme/static/img/favicon.ico'


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Qiskitdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Qiskit.tex', 'Qiskit Documentation',
     'Qiskit Development Team', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'qiskit', 'Qiskit Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Qiskit', 'Qiskit Documentation',
     author, 'Qiskit', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------


def setup(app):
    # Add the css required by sphinx-materialdesign-theme.
    app.add_stylesheet(
            html_theme_options['primary_color'],
            html_theme_options['accent_color']))
    app.add_stylesheet('sphinx_materialdesign_theme.css')
    # Add the custom css and js used by the Qiskit theme.
    app.add_stylesheet('css/theme.css')
    app.add_javascript('js/themeExt.js')
        """ % self.old_meta_version

        with open(os.path.join(self.tempdir.path,
                               'docs', 'conf.py'), 'w') as fd:
                fd.write(docs_conf_str)
