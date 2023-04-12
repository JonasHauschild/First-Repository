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

from Service.ServiceModellSarimax import ServiceModellSarimax

# Plot Zeitreihe
_mygraph_time_series = dcc.Graph(figure={})

# Erklärung zur Interpretation der Teststatistik (Text)
mytext_explain_test= dcc.Markdown(children='Hier steht die Erklärung der Statistik')
mytext_interpret_test= dcc.Markdown(children='Hier steht die Ergebnisinterpretation der Statistik')

statistical_analysis = html.Div([
    html.Div(children=[
        # Teststatistik auswählen
        html.Label('Teststatistik auswählen'),
        dcc.Dropdown(
            id='test_section',
            options=[
                # label (what users see) : value (passed into callback)
                {'label': 'ACF', 'value': 'ACF'},
                {'label': 'ACF', 'value': 'ACF'},
            ],
            placeholder='Select a test',
            clearable=False,
            multi=False
        ),
        #Zeilenumbruch durch Br
        html.Br(),
        #html.Div(children[
            html.Div('Choose Model'),
            # ROW
        dbc.Row([
            # Col 1
            dbc.Col([
                'Arimax',
                dcc.RadioItems(
                    options=[
                        {'label': 'Yes', 'value': 'Yes'},
                        {'label': 'No', 'value': 'No'},
                    ],
                value='No',
                inline=True,
                id='select_model_arimax',
                ),
            ]),
            #
            # COl 2
            dbc.Col([
                dbc.Collapse([
                    'Parameter 1: ',
                    dcc.Input(
                        id='input-circular', type='number', min=0, max=20, value=0
                    ),
                    'Parameter 2: ',
                    dcc.Input(
                        id='input-circular-2', type='number', min=0, max=20, value=0
                    ),
                ],
                id='collapse_parameter_arimax',
                is_open=False
                ),
            ]),
        ]),
            #
        #] style={'display': 'flex', 'flex.direction': 'row'})

    ], style={'padding': 10, 'flex': 1, 'border': '1px solid'}),
    html.Div(children=[
        _mygraph_time_series
    ], style={'padding': 10, 'flex': 1})
], style={'display': 'flex', 'flex-direction': 'row'})


def toggle_Arimax(is_selected, is_open):
    if is_selected:
        return not is_open
    return is_open
