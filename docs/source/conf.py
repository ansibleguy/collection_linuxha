from datetime import datetime

# pylint: disable=W0622

project = 'Ansible Collection - LinuxHA'
copyright = f'{datetime.now().year}, AnsibleGuy'
author = 'AnsibleGuy'
extensions = ['sphinx_rtd_theme']
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
# html_logo = ''
# html_favicon = ''
html_css_files = ['css/main.css']
master_doc = 'index'
display_version = True
sticky_navigation = True
source_suffix = {
    '.rst': 'restructuredtext',
}
html_theme_options = {}
