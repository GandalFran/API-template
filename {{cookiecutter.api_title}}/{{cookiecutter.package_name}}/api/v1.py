#!/usr/bin/python3

# Copyright {% now 'local', '%Y' %} {{cookiecutter.organization}}
# See LICENSE for details.
# Author: {{cookiecutter.author}} @{{cookiecutter.author_github}} on GitHub


from flask_restx import Api


api = Api(version='{{cookiecutter.api_version}}',
		  title='{{cookiecutter.api_title}}',
		  description="{{cookiecutter.api_description}}")