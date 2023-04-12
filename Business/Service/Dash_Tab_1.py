import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px

import pandas as pd

from Business.Service.ServiceModellSarimax import ServiceModellSarimax


upload_box = html.Div([
    dcc.Upload(
        id='upload_Data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-div'),  # tied to the second callback
    html.Div(id='output-datetable'),  # will hold return from first callback
    html.Div(id='output-modeldata')  # will hold the modelled data
])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),
        html.P('Insert X axis data'),
        dcc.Dropdown(id='xaxis-data',
                     options=[{'label':x,'value':x} for x in df.colums]),
        html.P('Insert Y axis data'),
        dcc.Dropdown(id='yaxis-data',
                     options=[{'label':x,'value':x} for x in df.colums]),
        html.Button(id='submit-button', children='Create Graph'),
        html.Hr(),

        dash_table.DataTable(
            data=df.todict('rocords'),
            columns=[{'name':i, 'id':i} for i in df.columns],
            page_size=15
        ),
        dcc.Store(id='stored-data', data=df.to_dict('records')),

        html.Hr(), # horizontel line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])