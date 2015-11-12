from pprint import pprint

import yaml
from wtforms import fields

from forms import Montecarlo

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


with open('/home/utkbansal/Downloads/config.yml', 'r') as f:
    doc = yaml.load(f)

    pprint(doc['montecarlo'])
    data = doc['montecarlo']
    print data.keys()

    for key in data.keys():
        if 'property_type' in data[key]:
            print data[key].get('help')
            field_type = field_map[data[key]['property_type']](
                default = data[key].get('default'),
                description= data[key].get('help'),
            )
            print field_type
            append_field(Montecarlo, key, field_type)


def get_leaves(cls, key, data):
    for key in data[key]:
        if type(data[key]) is dict:
            get_leaves(cls, key, data)
        else:
            print data[key]['property_type']
            append_field(cls, key, data[key]['property_type'])
