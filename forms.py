from wtforms import FormField
from wtforms import fields
from wtforms_tornado import Form


class TestForm(Form):
    name = fields.TextAreaField(description='bello')


class Supernova(Form):
    pass


class AtomData(Form):
    pass


class Plasma(Form):
    pass


class Montecarlo(Form):
    pass


class Spectrum(Form):
    pass


class ConfigForm(Form):
    supernova = FormField(Supernova)
    atom_data = FormField(AtomData)
    plasma = FormField(Plasma)
    montecarlo = FormField(Montecarlo)
    spectrum = FormField(Spectrum)
