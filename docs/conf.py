import datetime
import string



# Package information
project = "matc"
author = "Nattasit Phaisalrittiwong"
copyright = f"2022-{datetime.date.today().year}, {author}"


master_doc = "index"
language = None

# Output options
#html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_style = "css/style.css"
#html_logo = "logo.png"
html_show_sphinx = False
html_baseurl = "matc.org"
htmlhelp_basename = "matcdoc"
html_last_updated_fmt = ""

# Doc version sidebar
templates_path = ["_templates"]