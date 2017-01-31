# -*- coding: utf-8 -*-
#
# mappyfile documentation build configuration file, created by
# sphinx-quickstart on Fri Jan 13 00:17:15 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'mappyfile'
copyright = u'2017, S Girvin'
author = u'S Girvin'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'0.1'
# The full version, including alpha/beta/rc tags.
release = u'0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#
# today = ''
#
# Else, today_fmt is used as the format for a strftime call.
#
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
# html_title = u'mappyfile v0.1'

# A shorter title for the navigation bar.  Default is the same as html_title.
#
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
# html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
# html_last_updated_fmt = None

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#
#html_sidebars = {'**': ['globaltoc.html','searchbox.html','localtoc.html','relations.html']}
# 

html_logo = 'images/roll-36697_640.png'

# Additional templates that should be rendered to pages, maps page names to
# template names.
#
# html_additional_pages = {}

# If false, no module index is generated.
#
# html_domain_indices = True

# If false, no index is generated.
#
# html_use_index = True

# If true, the index is split into individual pages for each letter.
#
# html_split_index = False

# If true, links to the reST sources are added to the pages.
#
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh'
#
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'mappyfiledoc'

# -- Options for LaTeX output ---------------------------------------------

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
    (master_doc, 'mappyfile.tex', u'mappyfile Documentation',
     u'S Girvin', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#
# latex_use_parts = False

# If true, show page references after internal links.
#
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
#
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
#
# latex_appendices = []

# It false, will not define \strong, \code, 	itleref, \crossref ... but only
# \sphinxstrong, ..., \sphinxtitleref, ... To help avoid clash with user added
# packages.
#
# latex_keep_old_macro_names = True

# If false, no module index is generated.
#
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'mappyfile', u'mappyfile Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'mappyfile', u'mappyfile Documentation',
     author, 'mappyfile', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#
# texinfo_appendices = []

# If false, no module index is generated.
#
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#
# texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
# epub_basename = project

# The HTML theme for the epub output. Since the default themes are not
# optimized for small screen space, using the same theme for HTML and epub
# output is usually not wise. This defaults to 'epub', a theme designed to save
# visual space.
#
# epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or 'en' if the language is not set.
#
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#
# epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#
# epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#
# epub_pre_files = []

# HTML files that should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#
# epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#
# epub_tocdepth = 3

# Allow duplicate toc entries.
#
# epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#
# epub_tocscope = 'default'

# Fix unsupported image types using the Pillow.
#
# epub_fix_images = False

# Scale large images.
#
# epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
# epub_show_urls = 'inline'

# If false, no index is generated.
#
# epub_use_index = True

from pygments.lexer import RegexLexer, bygroups,combined, include
from pygments.token import *
from pygments import highlight
from pygments.formatters import HtmlFormatter


class WKTLexer(RegexLexer):
    name = 'wkt'
    aliases = ['wkt']
    filenames = ['*.wkt']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'[{}\[\]();,-.]+', Punctuation),
            (r'(PROJCS)\b', Generic.Heading),
            (r'(PARAMETER|PROJECTION|SPHEROID|DATUM|GEOGCS|AXIS)\b', Keyword),
            (r'(PRIMEM|UNIT|TOWGS84)\b', Keyword.Constant),
            (r'(AUTHORITY)\b', Name.Builtin),
            (r'[$a-zA-Z_][a-zA-Z0-9_]*', Name.Other),
            (r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            (r'0x[0-9a-fA-F]+', Number.Hex),
            (r'[0-9]+', Number.Integer),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
        ]
    }

import re
builtins = (r'(ANNOTATION|'
            r'AUTO|BEVEL|BITMAP|BUTT|CARTOLINE|CC|CENTER|'
            r'CHART|CIRCLE|CL|CONTOUR|CR|CSV|'
            r'DEFAULT|DD|ELLIPSE|EMBED|FALSE|FEET|FOLLOW|'
            r'GIANT|HATCH|HILITE|INCHES|KERNELDENSITY|KILOMETERS|LARGE|LC|'
            r'LEFT|LINE|LL|LOCAL|LR|MEDIUM|METERS|MILES|MITER|MULTIPLE|MYGIS|MYSQL|NONE|'
            r'NORMAL|OFF|OGR|ON|ONE-TO-ONE|ONE-TO-MANY|ORACLESPATIAL|'
            r'PERCENTAGES|PIXMAP|PIXELS|POINT|POLYGON|POSTGIS|POSTGRESQL|'
            r'PLUGIN|QUERY|RASTER|RIGHT|ROUND|SDE|SELECTED|SIMPLE|SINGLE|'
            r'SMALL|SQUARE|TINY|TRIANGLE|TRUE|TRUETYPE|UC|UL|UNION|UR|UV_ANGLE|UV_MINUS_ANGLE|UV_LENGTH|UV_LENGTH_2|UVRASTER|VECTOR|'
            r'WFS|WMS|ALPHA|'
            r'GIF|JPEG|JPG|PNG|WBMP|SWF|PDF|GTIFF|PC256|RGB|RGBA|INT16|FLOAT32|GD|'
            r'AGG|CAIRO|PNG8|SVG|KML|KMZ|GDAL|UTFGRID'
            r')\b')

keywords = (r'(ALIGN|'
            r'ALPHACOLOR|ANCHORPOINT|ANGLE|ANTIALIAS|AUTHOR|BACKGROUNDCOLOR|BACKGROUNDSHADOWCOLOR|'
            r'BACKGROUNDSHADOWSIZE|BANDSITEM|BROWSEFORMAT|BUFFER|CHARACTER|CLASS|CLASSITEM|'
            r'CLASSGROUP|CLUSTER|COLOR|COLORRANGE|COMPOSITE|COMPOP|COMPFILTER|CONFIG|CONNECTION|CONNECTIONTYPE|DATA|DATAPATTERN|DATARANGE|DEBUG|'
            r'DRIVER|DUMP|EMPTY|ENCODING|END|ERROR|EXPRESSION|EXTENT|EXTENSION|FEATURE|'
            r'FILLED|FILTER|FILTERITEM|FOOTER|FONT|FONTSET|FORCE|FORMATOPTION|FROM|GAP|GEOMTRANSFORM|'
            r'GRID|GRIDSTEP|GRATICULE|GROUP|HEADER|IMAGE|IMAGECOLOR|IMAGETYPE|IMAGEQUALITY|IMAGEPATH|'
            r'IMAGEURL|INCLUDE|INDEX|INITIALGAP|INTERLACE|INTERVALS|JOIN|KEYIMAGE|KEYSIZE|KEYSPACING|LABEL|'
            r'LABELCACHE|LABELFORMAT|LABELITEM|LABELMAXSCALE|LABELMAXSCALEDENOM|'
            r'LABELMINSCALE|LABELMINSCALEDENOM|LABELREQUIRES|LATLON|LAYER|LEADER|LEGEND|'
            r'LEGENDFORMAT|LINECAP|LINEJOIN|LINEJOINMAXSIZE|LOG|MAP|MARKER|MARKERSIZE|'
            r'MASK|MAXARCS|MAXBOXSIZE|MAXDISTANCE|MAXFEATURES|MAXINTERVAL|MAXSCALE|MAXSCALEDENOM|MINSCALE|'
            r'MINSCALEDENOM|MAXGEOWIDTH|MAXLENGTH|MAXSIZE|MAXSUBDIVIDE|MAXTEMPLATE|'
            r'MAXWIDTH|METADATA|MIMETYPE|MINARCS|MINBOXSIZE|MINDISTANCE|'
            r'MINFEATURESIZE|MININTERVAL|MINSCALE|MINSCALEDENOM|MINGEOWIDTH'
            r'MINLENGTH|MINSIZE|MINSUBDIVIDE|MINTEMPLATE|MINWIDTH|NAME|OFFSET|OFFSITE|'
            r'OPACITY|OUTLINECOLOR|OUTLINEWIDTH|OUTPUTFORMAT|OVERLAYBACKGROUNDCOLOR|'
            r'OVERLAYCOLOR|OVERLAYMAXSIZE|OVERLAYMINSIZE|OVERLAYOUTLINECOLOR|'
            r'OVERLAYSIZE|OVERLAYSYMBOL|PARTIALS|PATTERN|POINTS|POLAROFFSET|POSITION|POSTLABELCACHE|'
            r'PRIORITY|PROCESSING|PROJECTION|QUERYFORMAT|QUERYMAP|REFERENCE|REGION|'
            r'RELATIVETO|REQUIRES|RESOLUTION|SCALE|SCALEDENOM|SCALETOKEN|SHADOWCOLOR|SHADOWSIZE|'
            r'SHAPEPATH|SIZE|SIZEUNITS|STATUS|STYLE|STYLEITEM|SYMBOL|SYMBOLSCALE|'
            r'SYMBOLSCALEDENOM|SYMBOLSET|TABLE|TEMPLATE|TEMPLATEPATTERN|TEXT|'
            r'TILEINDEX|TILEITEM|TILESRS|TITLE|TO|TOLERANCE|TOLERANCEUNITS|TRANSPARENCY|'
            r'TRANSPARENT|TRANSFORM|TYPE|UNITS|UTFDATA|UTFITEM|WEB|WIDTH|WKT|WRAP|IMAGEMODE|VALIDATION|VALUES'
            r')\b')

class MapFileLexer(RegexLexer):
    name = 'mapfile'
    aliases = ['mapfile']
    filenames = ['*.map']

    flags = re.IGNORECASE
    tokens = {
        'root': [
            (r'\s+', Text),
            (r'\[.*?\]', Name.Other),
            (r'[{}\[\]();,-.]+', Punctuation),
            (r'#.*', Comment),
            (r'(AND|OR|NOT|EQ|GT|LT|GE|LE|NE|IN|IEQ)\b', Operator.Word),
            (r'!=|==|<=|>=|=~|&&|\|\||[-~+/*%=<>&^|./\$]', Operator),
            ('(?:[rR]|[uU][rR]|[rR][uU])"', String, 'dqs'),
            ("(?:[rR]|[uU][rR]|[rR][uU])'", String, 'sqs'),
            (r'`([^`])*`', Number.Date),
            ('[uU]?"', String, combined('stringescape', 'dqs')),
            ("[uU]?'", String, combined('stringescape', 'sqs')),
#            (constants, Keyword.Constant),
#            (r"""[]{}:(),;[]""", Punctuation),
            # (r'(MAP)\b', Generic.Heading),
            (keywords, Keyword),
            (builtins, Name.Builtin),
            (r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            (r'[0-9]+', Number.Integer),

        ],
        'dqs': [
            (r'"', String, '#pop'),
            (r'\\\\|\\"|\\\n', String.Escape), # included here again for raw strings
            include('strings')
        ],
        'sqs': [
            (r"'", String, '#pop'),
            (r"\\\\|\\'|\\\n", String.Escape), # included here again for raw strings
            include('strings')
        ],
        'tdqs': [
            (r'"""', String, '#pop'),
            include('strings'),
            include('nl')
        ],
        'tsqs': [
            (r"'''", String, '#pop'),
            include('strings'),
            include('nl')
        ],
        'strings': [
            (r'%(\([a-zA-Z0-9_]+\))?[-#0 +]*([0-9]+|[*])?(\.([0-9]+|[*]))?'
             '[hlL]?[diouxXeEfFgGcrs%]', String.Interpol),
            (r'[^\\\'"%\n]+', String),
            # quotes, percents and backslashes must be parsed one at a time
            (r'[\'"\\]', String),
            # unhandled string formatting sign
            (r'%', String)
            # newlines are an error (use "nl" state)
        ],
        'nl': [
            (r'\n', String)
        ],
        'stringescape': [
            (r'\\([\\abfnrtv"\']|\n|N{.*?}|u[a-fA-F0-9]{4}|'
             r'U[a-fA-F0-9]{8}|x[a-fA-F0-9]{2}|[0-7]{1,3})', String.Escape)
        ],
    }


def setup(app):
    from sphinx.highlighting import lexers
    lexers['wkt'] = WKTLexer()
    lexers['mapfile'] = MapFileLexer()

