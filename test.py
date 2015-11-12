from pprint import pprint

import yaml

with open('/home/utkbansal/Downloads/config.yml', 'r') as f:
    doc = yaml.load(f)

    pprint(doc)