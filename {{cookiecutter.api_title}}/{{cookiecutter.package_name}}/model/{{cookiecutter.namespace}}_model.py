#!/usr/bin/python3

# Copyright {% now 'local', '%Y' %} {{cookiecutter.organization}}
# See LICENSE for details.
# Author: {{cookiecutter.author}} @{{cookiecutter.author_github}} on GitHub

import math
import joblib 
import numpy as np
import pandas as pd


class {{cookiecutter.namespace}}Model:
    
    # CONSTRUCTOR-------------------------------------------------

    def __init__(self, path='./{{cookiecutter.package_name}}/model/{{cookiecutter.model_name}}'):

        try:
            # load the model
            self.model = joblib.load(path)
        except:
            raise KeyError("FAIL TO LOAD THE MODEL")

    # METHODS--------------------------------------------------

    def predict(self, data):
        return self.model.predict(data)