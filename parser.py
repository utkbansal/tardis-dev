import os
from pprint import pprint

import yaml
from wtforms import fields

from forms import ConfigForm
from settings import BASE_DIR

field_map = {
    'quantity': fields.FloatField,
    'string': fields.StringField,
    'bool': fields.BooleanField,
    'float': fields.FloatField,
    'int': fields.IntegerField,
    'quantity_range_sampled': fields.TextAreaField,
    'list': fields.TextAreaField,
}


def append_field(cls, name, field):
    setattr(cls, name, field)

    return cls


def recursive_parse(data):
    if type(data) is dict:
        for key in data.keys():
            if 'mandatory' in data[key]:
                pprint(key)
                pprint(data[key]['property_type'])
                pprint(data[key])
                print 'error at ', key
                field_type = field_map[data[key]['property_type']](
                    default=data[key].get('default'),
                    description=data[key].get('help'),
                    # render_kw={'a': 22129213},
                    # validators = [validators.required()]
                )
                # print field_type
                append_field(ConfigForm, key, field_type)
            else:
                print 'calling', data[key]
                recursive_parse(data[key])


def populate_form_class():
    with open(os.path.join(os.environ['HOME'], 'config.yml'), 'r') as f:
        doc = yaml.load(f)
        recursive_parse(doc)
        # pprint(doc['montecarlo'])
        # data = doc['montecarlo']
        # print data.keys()

        # for key in data.keys():
        #     if 'property_type' in data[key]:
        #         # print data[key].get('help')
        #         field_type = field_map[data[key]['property_type']](
        #             default=data[key].get('default'),
        #             description=data[key].get('help'),
        #             render_kw={'a': 22129213},
        #             # validators = [validators.required()]
        #         )
        #         # print field_type
        #         append_field(ConfigForm, key, field_type)


def get_leaves(cls, key, data):
    for key in data[key]:
        if type(data[key]) is dict:
            get_leaves(cls, key, data)
        else:
            # print data[key]['property_type']
            append_field(cls, key, data[key]['property_type'])


test_dict = {
    'plasma': {
        'property_type': 'x'
    },
    'xyz': {
        'abc': {
            'property_type': 'x'
        },
        'def': {
            'geh': {
                'property_type': 'x'
            }
        }
    }
}




    # pprint(doc)

#
# with open('/home/utkbansal/config.yml', 'r') as f:
#     doc = yaml.load(f)
#     recursive_parse(doc)
