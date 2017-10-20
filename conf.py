# Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2017. Part of mess
# -*- coding: utf-8 -*-

# read STD config ...
#==========================================
import sys; sys.path.append('_external_templates/conf')
from std_conf import *


extensions.append('sphinx.ext.autodoc')                                 # Move to std_conf?
autodoc_member_order='bysource'
import os.path
sys.path.append(os.path.join('BureauLade','dPID'))

# General information about the project.
#======================================
project = 'MESS-DocIdeas'
copyright = "ALbert Mietus, 2017"

from datetime import datetime
release = datetime.now().strftime("%Y%m%d.%H")
version = release

# Overrule std_conf, where needed
#================================

html_title = project + " | " + release # DEFAULT: '<project> v<revision> documentation' -- Strip "documentation"


# plantUML
#---------
if not on_rtd:
    extensions.append('sphinxcontrib.plantuml')
    plantuml = 'java -jar /Users/albert/Apps/PlantUML/libexec/plantuml.jar -nogui'



