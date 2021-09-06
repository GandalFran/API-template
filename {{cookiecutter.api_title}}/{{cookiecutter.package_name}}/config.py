#!/usr/bin/python3

# Copyright {% now 'local', '%Y' %} {{cookiecutter.organization}}
# See LICENSE for details.
# Author: {{cookiecutter.author}} @{{cookiecutter.author_github}} on GitHub


class Config:
    DEBUG = True
    PORT = 5000
    HOST = '0.0.0.0'
    URL_PREFIX = '/{{cookiecutter.api_title}}/{{cookiecutter.namespace}}/v1'

    CACHE_TYPE = 'simple' # to follow simple cache strategy
    CACHE_DEFAULT_TIMEOUT = 10 * 60 # time expiration: 10 minutes

    RATELIMIT_HEADERS_ENABLED = True
