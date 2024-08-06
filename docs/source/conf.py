from datetime import datetime

# pylint: disable=W0622

project = 'Ansible Collection - LinuxHA'
copyright = f'{datetime.now().year}, AnsibleGuy'
author = 'AnsibleGuy'
extensions = ['piccolo_theme']
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'piccolo_theme'
html_static_path = ['_static']
html_logo = 'https://clusterlabs.org/assets/clusterlabs3-9dbb18813995af518cd0b823b0eaaa83b4ba5770f199728d37818b090f1f377c.svg'
html_favicon = '_static/img/favicon.ico'
html_css_files = ['css/main.css']
master_doc = 'index'
display_version = True
sticky_navigation = True
source_suffix = {
    '.rst': 'restructuredtext',
}
html_theme_options = {
    'banner_text': 'Check out <a href="https://github.com/ansibleguy/collection_linuxha">the repository on GitHub</a> | '
                   'Report <a href="https://github.com/ansibleguy/collection_linuxha/issues/new/choose">missing/incorrect information or broken links</a>'
}
html_short_title = 'Ansible LinuxHA'