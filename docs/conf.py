"""Sphinx configuration."""
from datetime import datetime


project = "HANMATEK Power Supplies (HM305, HM310, HM310p, RS605p)"
author = "Christian Stenzel"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "sphinx_rtd_theme",
]
autodoc_typehints = "description"
html_theme = "sphinx_rtd_theme"
