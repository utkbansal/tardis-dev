import os
from pprint import pprint

import yaml
from wtforms import fields, validators

from forms import ConfigForm
from settings import BASE_DIR

field_map = {
    'quantity': fields.FloatField,
    'string': fields.StringField,
    'bool': fields.BooleanField,
    'float': fields.FloatField,
    'int': fields.IntegerField,
    'quantity_range_sampled': fields.TextAreaField,
}


def append_field(cls, name, field):
    setattr(cls, name, field)

    return cls



def populate_form_class():
    with open(os.path.join(BASE_DIR, 'config.yml'), 'r') as f:
        doc = yaml.load(f)

        # pprint(doc['montecarlo'])
        data = doc['montecarlo']
        # print data.keys()

        for key in data.keys():
            if 'property_type' in data[key]:
                # print data[key].get('help')
                field_type = field_map[data[key]['property_type']](
                    default=data[key].get('default'),
                    description=data[key].get('help'),
                    render_kw={'a': 22129213},
                    # validators = [validators.required()]
                )
                # print field_type
                append_field(ConfigForm, key, field_type)


def get_leaves(cls, key, data):
    for key in data[key]:
        if type(data[key]) is dict:
            get_leaves(cls, key, data)
        else:
            # print data[key]['property_type']
            append_field(cls, key, data[key]['property_type'])
