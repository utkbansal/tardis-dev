import StringIO
import os

import yaml

from settings import BASE_DIR


def create_yaml(data):
    with open(os.path.join(BASE_DIR, 'config.yml'), 'r') as f:
        doc = yaml.load(f)

        # pprint(doc['montecarlo'])

        yaml_dict = {}

        yaml_dict['montecarlo'] = doc['montecarlo']

        for key in doc['montecarlo']:
            if key in data:
                yaml_dict['montecarlo'][key] = data[key][0]

        # pprint(yaml_dict)

        yaml_file = StringIO.StringIO()
        yaml_file.write(yaml.safe_dump(yaml_dict, default_flow_style=False))

        return yaml_file
