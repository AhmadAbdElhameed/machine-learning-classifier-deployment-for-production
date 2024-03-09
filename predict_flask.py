#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 03:21:52 2024

@author: ahmad
"""

import pickle

from flask import Flask , request
from flasgger import Swagger
import numpy as np
import pandas as pd

with open('./rf.pkl','rb') as model_file:
    model = pickle.load(model_file);
    
app = Flask(__name__)
swagger = Swagger(app)

@app.route('/predict')
def predict():
    """
    Example Endpoint returning prediction of iris
    ---
    parameters:
        - name: s_length
          in: query
          type: integer
          required: true
        - name: s_width
          in: query
          type: integer
          required: true
        - name: p_length
          in: query
          type: integer
          required: true
          
        - name: p_width
          in: query
          type: integer
          required: true
    responses:
      200:
        description: "0: Iris-setosa, 1: Iris-versicolor, 2: Iris-virginica"
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
            examples:
              message:
                value: {"msg": "Success"}
    """
    s_length = request.args.get('s_length')
    s_width = request.args.get('s_width')
    p_length = request.args.get('p_length')
    p_width = request.args.get('p_width')
    prediction = model.predict(np.array([[s_length,s_width,
                                         p_length,p_width]]))
    return str(prediction)



@app.route('/predict_file',methods=['POST'])
def predict_file():
    """
    Example File Endpoint returning prediction of iris
    ---
    parameters:
        - name: input_file
          in: formData
          type: file
          required: true
    responses:
      200:
        description: "0: Iris-setosa, 1: Iris-versicolor, 2: Iris-virginica"
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
            examples:
              message:
                value: {"msg": "Success"}
    """
    input_data = pd.read_csv(request.files.get('input_file'),header=None)
    prediction = model.predict(input_data)
    return str(list(prediction))



if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)