import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table
import plotly.express as px

import pandas as pd

import Service.Dash_Tab_2
from Service.ServiceModellSarimax import ServiceModellSarimax

from Business.Service.Dash_Tab_1 import upload_box
from Business.Service.Dash_Tab_2 import statistical_analysis

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_scripts=external_stylesheets,
                suppress_callback_exceptions=True)

app.layout = html.Div([ # this code section taken from Dash docs https://dash.plotly.com/dash-core-components/upload
    html.H1('Einlagenmodellierung'),
    dcc.Tabs([
        dcc.Tab(label='Input and View Data', children= [
            upload_box
        ]),
        dcc.Tab(label='Statistical Analysis and Model Parameters', children= [
            statistical_analysis
        ]),
        dcc.Tab(label='Forecasting', children= [
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1,2,3], 'y': [2,3,4],
                         'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [5, 4, 3],
                         'type': 'bar', 'name': u'Montreal'},
                    ]
                }
            )
        ]),
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)