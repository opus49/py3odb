# -- Project information -----------------------------------------------------
project = 'py3odb'
copyright = '2019, U.S. Federal Government (in countries where recognized)'
author = 'Mike Puskar'
release = "0.3"
version = release
master_doc = 'index'


# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx_rtd_theme',
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_show_sphinx = False
html_show_sourcelink = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
