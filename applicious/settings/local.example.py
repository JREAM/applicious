"""
Local Settings
This file is to be renamed 'local.py', this file is in the .gitignore

For local/development change to:  from .development import *
For staging change to:            from .staging import *
For production change:            from .production import *
"""
from .development import *

SECRET_KEY = 'jke_rmx*a-ov9g=qk=arlkqguh8-994ycfbt1q12xuhwq#=e85'

# APPS = ('your_apps',)
# INSTALLED_APPS += APPS
# DATABASES= {}
