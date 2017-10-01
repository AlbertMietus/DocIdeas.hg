# Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2011-2013, 2015
# SwBMnl theme configuration
# -*- coding: utf-8 -*-

##
## Use SwBMnl colors/fonts
##
_SwBMnl_BLAUW  = '#000066'
_SwBMnl_LBLAUW = '#eeeeff'
_SwBMnl_ROOD   = '#cc3333'
_SwBMnl_LTROOD = '#ffcccc'
_SwBMnl_SILVER = '#c0c0c0'
_SwBMnl_GRAY   = '#808080'
_SwBMnl_Black  = '#000000'
_SwBMnl_White  = '#ffffff'

html_theme_options = {
    ## Options
    'collapsiblesidebar' : True,
    'externalrefs'       : True,
    'stickysidebar'      : True,

    ## fonts # (CSS font-family):
    'bodyfont' : '"Georgia", "Times New Roman", "Times"',
    'headfont' : '"Georgia", "Times New Roman", "Times"',

    ## Color's (CSS color)
    'bgcolor'		: _SwBMnl_LBLAUW,	#  Body background color.
    'textcolor'		: _SwBMnl_Black,	#  Body text color.
    'linkcolor'		: _SwBMnl_BLAUW,	#  Body link color.
    'visitedlinkcolor'	: _SwBMnl_BLAUW,	#  Body color for visited links.

    'headbgcolor'	: _SwBMnl_LBLAUW,	#  Background color for headings.
    'headtextcolor'	: _SwBMnl_BLAUW,	#  Text color for headings.
    'headlinkcolor'	: _SwBMnl_BLAUW,	#  Link color for headings.

    'sidebarbgcolor'	: _SwBMnl_BLAUW,	#  Background color for the sidebar.
    'sidebartextcolor'	: _SwBMnl_White, 	#  Text color for the sidebar.
    'sidebarlinkcolor'	: _SwBMnl_LBLAUW,	#  Link color for the sidebar.
    'sidebarbtncolor'	: _SwBMnl_BLAUW,	#  Background color for the sidebar collapse button (used when collapsiblesidebar is true).

    'relbarbgcolor'	: _SwBMnl_BLAUW,	#  Background color for the relation bar(s). ( high & low h-bars)
    'relbartextcolor'	: _SwBMnl_LBLAUW,	#  Text color for the relation bar.
    'relbarlinkcolor'	: _SwBMnl_White,	#  Link color for the relation bar.

    'codebgcolor'	: _SwBMnl_SILVER,	#  Background color for code blocks.
    'codetextcolor'	: _SwBMnl_BLAUW,	#  Default text color for code blocks, if not set differently by the highlighting style.

    'footerbgcolor'	: _SwBMnl_SILVER,	#  Background color for the footer line.
    'footertextcolor'	: _SwBMnl_BLAUW,	#  Text color for the footer line.

    }
