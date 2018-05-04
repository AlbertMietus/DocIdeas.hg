# Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2017, 2018
# -*- coding: utf-8 -*-

# read STD config ...
#==========================================
import sys; sys.path.append('_external_templates/conf')
from std_conf import *

# General information about the project.
#======================================
project = 'DocIdeas'
copyright = "ALbert Mietus, 2018"

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

## ABlog
#-------
extensions.append('ablog')

import ablog; templates_path.append(ablog.get_html_templates_path())

blog_path="Blog"
fontawesome_link_cdn = "https://use.fontawesome.com/releases/v5.0.10/css/all.css"

post_date_format = '%Y/%m/%d'
post_date_format_short = '%Y/%m'

blog_authors = {'GAM' : ('ALbert Mietus', 'http://albert.mietus.nl') }
blog_default_author = 'GAM'
blog_languages = {
    'nl'  : ('Nederlands', None),
    'en'  : ('English', None) }
blog_default_language = 'nl'
post_always_section = True


blog_baseurl = "/" # XXX



# Autodoc
#---------
extensions.append('sphinx.ext.autodoc')                                 # Move to std_conf?
autodoc_member_order='bysource'



# plantUML
#---------
extensions.append('sphinxcontrib.plantuml')
if not on_rtd:
    plantuml = 'java -jar /Users/albert/Apps/PlantUML/libexec/plantuml.jar -nogui'




def setup(app):
    app.add_stylesheet('../_static/SwBMnl+rtfd.css')

