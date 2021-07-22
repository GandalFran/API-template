#!/usr/bin/python3

# Copyright {% now 'local', '%Y' %} {{cookiecutter.organization}}
# See LICENSE for details.
# Author: {{cookiecutter.author}} @{{cookiecutter.author_github}} on GitHub


from flask_restx import fields

from {{cookiecutter.package_name}}.run import api


{{cookiecutter.namespace}}_nested_model = api.model('ExampleNestedModel',{
    'param1': fields.Integer()
}, description='example nested model')


{{cookiecutter.namespace}}_input_model = api.model('PredictionInput', {
    'floatparam': fields.Float(description='Description of parameter', required=False, example=7.0, default=7.0),
    'intparam': fields.Integer(description='Description of parameter', required=True, example=10),
    'strparam': fields.String(description='Description of parameter', required=True, example='example'),
    'dtparam': fields.DateTime(dt_format='iso8601', description='Description of parameter', required=True, example='2021-07-21T19:37:06+0000'),
    'nestedparam': fields.Nested({{cookiecutter.namespace}}_nested_model, skip_none=True, allow_null=False, description='Descripcion of parameter'),
    'listparam': fields.List(fields.Integer(),description="Description of parameter", example=[1,2,3])
}, description="Input parameters used to predict the amount of sulphates")


{{cookiecutter.namespace}}_output_model = api.model('PredictionOutput', {
    'param1': fields.Float(description='Description of parameter', required=True, example=1.0),
    'param2': fields.Float(description='Description of parameter', required=True, example=1.0)
}, description="Results of the prediction of sulphate levels")
