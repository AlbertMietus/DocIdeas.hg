# Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2017- 2024
# -*- coding: utf-8 -*-

DEBUG=False

# read STD config ...
#==========================================
import sys; sys.path.append('_external_templates/conf')
from std_conf import *

# General information about the project.
#======================================
project = 'DocIdeas'
copyright = "ALbert Mietus, 2018 - 2024"

from datetime import datetime
release = datetime.now().strftime("%Y%m%d.%H")
version = release

# Overrule std_conf, where needed
#================================

html_title = project + " | " + release # DEFAULT: '<project> v<revision> documentation' -- Strip "documentation"

html_sidebars = {'**': [ 'postcardHeader.html', # empty when no blog!
                         'recentposts.html',
                         'categories.html',
                         'tagcloud.html']}
def setup(app):
    app.add_css_file('../_static/SwBMnl+rtfd.css')
    app.add_css_file('../_static/std_needs.css')

#Does not work on Safari ...
html_static_path.append ('_static/')
html_favicon = '_static/Bulb.ico'

exclude_patterns.append('**/LinkToOrg/**')

## ABlog
#-------
extensions.append('ablog')

blog_path="ABlog"
fontawesome_link_cdn = "https://use.fontawesome.com/releases/v5.0.10/css/all.css"

post_date_format = '%Y/%m/%d'
post_date_format_short = '%Y/%m'

blog_authors = {'GAM' : ('ALbert Mietus', 'http://albert.mietus.nl') }
blog_default_author = 'GAM'
blog_languages = {
    'nl'  : ('Nederlands', None),
    'en'  : ('English', None)
}
blog_default_language = 'en'
language='en' # As workaround for ABlog.post.generate_atom_feeds -- see: https://github.com/sunpy/ablog/issues/137
post_always_section = True


blog_baseurl = "http://DocIdeas.Mietus.nl/"
disqus_shortname = 'DocIdeas'
disqus_pages = True                                                 # All pages have a disqus-section
disqus_drafts = False                                               # .. but the draft (blog) pages (.. post:: without date )


# Autodoc
#---------
extensions.append('sphinx.ext.autodoc')                                 # Move to std_conf?
autodoc_member_order='bysource'



# plantUML
#---------
plantuml_output_format='png' ## dito only can be png?




# tabs (There are many versions, we use this one: https://sphinx-tabs.readthedocs.io/
#-----------------------------------------------
extensions.append('sphinx_tabs.tabs')

html_theme_options["navigation_depth"] =5

if DEBUG:
    print("Debug: show all packages:")
    import os
    os.system("pip list")
    print("Debug: Outdates packages:")
    os.system("pip list --outdated")
    print("Done =====")


if True:
    print("""Using a WORKAROUND for
    /Users/albert/work/DocIdeas,hg/CCastle/2.Analyse/8.ConcurrentComputingConcepts.rst:14: WARNING: unknown node type: <NeedRef: <emphasis...>>
    Theme error:
    An error happened in rendering the page ABlog/author/albert-mietus.
    Reason: NotImplementedError("<class 'sphinx.writers.html5.HTML5Translator'> departing unknown node type: NeedRef")
""")
    from sphinx.writers.html5 import HTML5Translator

    if not hasattr(HTML5Translator, 'depart_NeedRef'):
        HTML5Translator.depart_NeedRef = lambda self, node: None
    if not hasattr(HTML5Translator, 'visit_NeedRef'):
        HTML5Translator.visit_NeedRef = lambda self, node: None
