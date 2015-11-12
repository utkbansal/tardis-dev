import os

from jinja2 import FileSystemLoader, Environment

BASE_DIR = (os.path.dirname(__file__))

TEMPLATE_ROOT = os.path.join(BASE_DIR, 'templates')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

print BASE_DIR
print TEMPLATE_ROOT

jinja_settings = {
    'autoescape': True,
}

jinja_env = Environment(loader=FileSystemLoader(TEMPLATE_ROOT),
                        **jinja_settings)
