from flask import render_template, request, jsonify
from . import pypivot

import numpy as np
import pandas as pd

@pypivot.route('/')
def index():
    global df
    df = pd.read_csv("http://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/Males.csv")
    #df = pd.DataFrame(np.random.randn(20, 10))
    print(df.describe())
    #return  render_template('pandaspage.html', pandastable=df, np=np)
    return render_template('pypivot/index.html', pandastable=df, np=np)

@pypivot.route('/pivot',  methods=['GET', 'POST'])
def pivot():
    filters = request.form.getlist("filters[]")
    rows = request.form.getlist("rows[]")
    columns = request.form.getlist("columns[]")
    values = request.form.getlist("values[]")
    print(df.head())
    print("starting pivot here")
    pivot = pd.pivot_table(df, values=values, index=rows, columns=columns, aggfunc=[np.sum, np.mean, np.count_nonzero], fill_value=None, margins=False, dropna=True)
    print(filters, rows, columns, values)
    print(pivot)
    return jsonify(success=True, data=pivot.to_html(classes="table table-striped table-condensed table-hover", na_rep="-"))

