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
exclude_patterns = ['**/.#*', '**/_*', 'VENV']
html_static_path = ['_external_templates/static/']
templates_path = ['_templates']

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

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': True,
    'display_version': True,
    #    'style_external_links': False, # available in next release
    'prev_next_buttons_location': 'both',
}
html_style = 'SwBMnl+rtfd.css'


# sphinx.ext.todo
#-----------------
extensions.append('sphinx.ext.todo')
todo_include_todos=True


# Needs
#------
extensions.append('sphinxcontrib.needs')
needs_include_needs = True
needs_id_required = True
needs_id_regex = r'^[A-Z][A-Za-z]*_[A-Za-z0-9-]{2,}'


from std_needs import needs_types, needs_layouts
needs_default_layout = 'clean_collapsed'

if True
    print("Debug: show all packages:")
    import os
    os.system("pip list")
    print("Debug: Outdates packages:")
    os.system("pip list --outdated")
    print("Done =====")
