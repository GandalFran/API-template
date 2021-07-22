#!/usr/bin/python3

# Copyright {% now 'local', '%Y' %} {{cookiecutter.organization}}
# See LICENSE for details.
# Author: {{cookiecutter.author}} @{{cookiecutter.author_github}} on GitHub


import flask
import datetime
import pandas as pd
from flask_restx import Resource

from {{cookiecutter.package_name}}.run import api
from {{cookiecutter.package_name}}.core import cache, limiter
from {{cookiecutter.package_name}}.utils import handle400error, handle404error, handle500error

from {{cookiecutter.package_name}}.model.{{cookiecutter.namespace}}_model import {{cookiecutter.namespace}}Model
from {{cookiecutter.package_name}}.api.{{cookiecutter.namespace}}_parsers import {{cookiecutter.namespace}}_parser 
from {{cookiecutter.package_name}}.api.{{cookiecutter.namespace}}_models import {{cookiecutter.namespace}}_input_model, {{cookiecutter.namespace}}_output_model


{{cookiecutter.namespace}}_ns = api.namespace('{{cookiecutter.namespace}}', description='Provides {{cookiecutter.namespace}} funcionality')


model = {{cookiecutter.namespace}}Model()


@{{cookiecutter.namespace}}_ns.route('/prediction')
class {{cookiecutter.namespace}}Prediction(Resource):

    @api.expect({{cookiecutter.namespace}}_input_model)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @api.marshal_with({{cookiecutter.namespace}}_output_model, code=200, description='OK', as_list=False)
    @limiter.limit('1000000/hour') 
    @cache.cached(timeout=1, query_string=True)
    def post(self):
        """
        Performs a prediction.
        """
        
        global model

        # retrieve arguments
        try:
            obj = flask.request.get_json()
        except:
            return handle400error({{cookiecutter.namespace}}_ns, 'Unable to retrieve arguments from request. Please, check the swagger documentation at /v1')

        # check parameters
        try:
            params = {{cookiecutter.namespace}}_parser.parse_args()
        except:
            return handle400error(example_ns, 'Malformed request. Please, check the request at /v1')

        # build recomendation 
        try:
            param1, param2 = model.predict(params)
        except:
            return handle500error({{cookiecutter.namespace}}_ns)

        # build result
        result_prediction = {
            'param1': float(param1),
            'param2': float(param2)
        }

        return result_prediction
