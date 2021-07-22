#!/usr/bin/python3

# Copyright {% now 'local', '%Y' %} {{cookiecutter.organization}}
# See LICENSE for details.
# Author: {{cookiecutter.author}} @{{cookiecutter.author_github}} on GitHub


from flask_restx import reqparse, inputs


{{cookiecutter.namespace}}_parser = reqparse.RequestParser()

{{cookiecutter.namespace}}_parser.add_argument('floatparam', location='json', type=float, required=False, help='missing floatparam')
{{cookiecutter.namespace}}_parser.add_argument('intparam', location='json', type=int, required=True, help='missing intparam')
{{cookiecutter.namespace}}_parser.add_argument('strparam', location='json', type=str, required=True, help='missing strparam')
{{cookiecutter.namespace}}_parser.add_argument('dtparam', location='json', type=inputs.date_from_iso8601, required=True, help='missing dtparam')
{{cookiecutter.namespace}}_parser.add_argument('nestedparam', location='json', type=dict, required=True, help='missing nestedparam')
{{cookiecutter.namespace}}_parser.add_argument('listparam', location='json', type=list, required=True, help='missing listparam')