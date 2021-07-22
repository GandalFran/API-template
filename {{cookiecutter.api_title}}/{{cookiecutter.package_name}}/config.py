#!/usr/bin/python3

# Copyright {% now 'local', '%Y' %} {{cookiecutter.organization}}
# See LICENSE for details.
# Author: {{cookiecutter.author}} @{{cookiecutter.author_github}} on GitHub


import os


# api config
PORT = 5000
HOST = '0.0.0.0'
URL_PREFIX = '/{{cookiecutter.api_title}}/{{cookiecutter.namespace}}/v1'
DEBUG_MODE = True