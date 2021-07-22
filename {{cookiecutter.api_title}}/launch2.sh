#!/bin/bash
# Copyright {% now 'local', '%Y' %} {{cookiecutter.organization}}
# See LICENSE for details.
# Author: {{cookiecutter.author}} @{{cookiecutter.author_github}} on GitHub

sudo python3 -m pip install pip --upgrade
sudo python3 setup.py install --force
sudo {{cookiecutter.package_name}}