#!/usr/bin/python3

# Copyright {% now 'local', '%Y' %} {{cookiecutter.organization}}
# See LICENSE for details.
# Author: {{cookiecutter.author}} @{{cookiecutter.author_github}} on GitHub

import math
import joblib 
import numpy as np
import pandas as pd


class {{cookiecutter.namespace}}Model:
    
    def predict(self, params):
        return 1.0, 2.0