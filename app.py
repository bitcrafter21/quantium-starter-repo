# app.py
import dash
from dash import html, dcc
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Quantium Data Visualisation"),
    dcc.Graph(id='example-graph')
])

if __name__ == '__main__':
    app.run(debug=True)
