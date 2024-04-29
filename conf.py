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

extensions.append('sphinxcontrib.plantuml')
if on_rtd:
    #  in `.readthedocs.yaml`
    #     post_install:
    #      - curl -o ${READTHEDOCS_VIRTUALENV_PATH}/libexec/plantuml.jar -L https://github.com/plantuml/....
    # Make use of that plantUML version
    import os
    _path=os.environ['READTHEDOCS_VIRTUALENV_PATH'] + '/libexec/'
    plantuml = f'java  -Djava.awt.headless=true  -jar {_path}plantuml.jar'
    #print(f'DEBUG: plantuml={plantuml}')
else: #local
    plantuml = 'java  -Djava.awt.headless=true  -jar /Users/albert/Apps/PlantUML/libexec/plantuml-1.2024.4.jar' # NEW


##plantuml_output_format='svg_img'
## dito only can be png?
plantuml_output_format='png'

plantuml_syntax_error_image=True
if True or DEBUG:
    import subprocess
    result = subprocess.run(plantuml.split() +['-version'], stdout=subprocess.PIPE)
    print(f"Using plantuml -version: {result.stdout}")



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
