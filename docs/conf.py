import os
import sys
from datetime import datetime

# Add src to sys.path for autodoc
sys.path.insert(0, os.path.abspath("../src"))

project = "package_template"
author = "Your Name"
current_year = datetime.now().year
copyright = f"{current_year}, {author}"

# -- General configuration ------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "myst_parser",
    "sphinx_gallery.gen_gallery",
]

autosummary_generate = True
napoleon_google_docstring = False
napoleon_numpy_docstring = True

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

# -- Options for HTML output ----------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]

# MyST settings
myst_enable_extensions = [
    "deflist",
    "fieldlist",
    "colon_fence",
]

# Sphinx-gallery configuration
sphinx_gallery_conf = {
    "examples_dirs": ["examples"],
    "gallery_dirs": ["auto_examples"],
    "filename_pattern": r"/plot_.*\.py$",
    "download_all_examples": False,
}
