import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html
from dash import dash_table
import plotly.express as px

import pandas as pd

import ServiceModellSarimax
#from Service.ServideModellSarimax import ServiceModellSarimax


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_scripts=external_stylesheets,
                suppress_callback_exceptions=True)

app.layout = html.Div([ # this code section taken from Dash docs https://dash.plotly.com/dash-core-components/upload
    dcc.Upload(
        id='upload-data',
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
    html.Div(id='output-div'), # tied to the second callback
    html.Div(id='output-datetable'), # will hold return from first callback
    html.Div(id='output-modeldata') # will hold the modelled data
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

@app.callback(Output('output-datatable', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


@app.callback(Output('output-div', 'children'),
              Input('submit-button', 'n_clicks'),
              State('stored-data', 'data'),
              State('xaxis-data', 'value'),
              State('yaxis-data', 'value'))
def make_graphs(n, data, x_data, y_data):
    if n is None:
        return dash.no_update
    else:
        bar_fig = px.line(data, x=x_data, y=y_data)
        #print(data)
        return dcc.Graph(figure=bar_fig),\
            html.Button(id='model-button', children='Modellierte Zeitreihe'),\
            html.Hr()

@app.callback(Output('output-modeldata', 'children'),
              Input('model-button', 'n_clicks'),
              State('stored-data', 'data'),
              State('xaxis-data', 'value'),
              State('yaxis-data', 'value'))
def modelliere(n, data, xaxix, yaxis):
    if n is None:
        return dash.no_update
    else:
        df = pd.DataFrame(data)

        # Modellierung
        _model = ServiceModellSarimax(data=df, xcol=xaxix, ycol=yaxis)
        _model.run()

        return

if __name__ == '__main__':
    app.run_server(debug=True)

