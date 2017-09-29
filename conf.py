# Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2017. Part of mess
# -*- coding: utf-8 -*-

# read STD config ...
#==========================================
#import sys; sys.path.append('../_external_templates/conf')
#from std_conf import *


# General information about the project.
#======================================
project = 'MESS'
copyright = "ALbert Mietus, 2017"
version = "None"

# Overrule std_conf, where needed
#================================

release = version
html_title = project + " | " + release # DEFAULT: '<project> v<revision> documentation' -- Strip "documentation"


# plantUML
#---------
if not on_rtd:
    extensions.append('sphinxcontrib.plantuml')
    plantuml = 'java -jar /Users/albert/Apps/PlantUML/libexec/plantuml.jar -nogui'