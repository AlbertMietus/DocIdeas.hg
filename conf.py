# Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2017, 2018
# -*- coding: utf-8 -*-

# read STD config ...
#==========================================
import sys; sys.path.append('_external_templates/conf')
from std_conf import *

# General information about the project.
#======================================
project = 'DocIdeas'
copyright = "ALbert Mietus, 2018 - 2022"

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


blog_baseurl = "http://DocIdeas.Mietus.nl"
disqus_shortname = 'DocIdeas'
disqus_pages = True                                                 # All pages have a disqus-section
disqus_drafts = False                                               # .. but the draft (blog) pages (.. post:: without date )


# Autodoc
#---------
extensions.append('sphinx.ext.autodoc')                                 # Move to std_conf?
autodoc_member_order='bysource'



# plantUML
#---------
extensions.append('sphinxcontrib.plantuml')
if not on_rtd:
    plantuml = 'java -jar /Users/albert/Apps/PlantUML/libexec/plantuml.jar -nogui'




# tabs (There are many versions, we use this one
#-----------------------------------------------
extensions.append('sphinx_tabs.tabs')

