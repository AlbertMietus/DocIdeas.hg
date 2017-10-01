# Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2011-2017
#  STANDARD CONFiguration for Sphinx-doc
# -*- coding: utf-8 -*-

import os
on_rtd = os.environ.get('READTHEDOCS') == 'True'

print("Using std_conf [%s-version]" % ('RTfD' if on_rtd else 'local'))

###
### File/Project layout
###

master_doc = 'index'
source_suffix = '.rst'
exclude_patterns = ['**/.#*', '**/_*']
html_static_path = ['_external_templates/static/']
templates_path = ['templates']

###
### Kick off
###
try:    extensions = extensions
except NameError: extensions=[]

show_authors = False # Always me

rst_epilog = None
rst_prolog = """
.. include:: /_generic.inc

"""

###
### Normal HTML output
###

html_theme = 'classic'
html_style = 'SwBMnl-sphinx.css'

# HTML-Slides (using Hieroglyph)
#-------------------------------
extensions.append('hieroglyph')

slide_theme = 'slides'
slide_levels = 2

slide_theme_options = {'custom_css': 'SwBMnl-hieroglyph_slides=article.css'}

slide_link_to_html=False
slide_link_html_to_slides=False


# sphinx.ext.todo
#-----------------
extensions.append('sphinx.ext.todo')
todo_include_todos=True
