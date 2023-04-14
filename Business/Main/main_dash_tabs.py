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
                     options=[{'label':x,'value':x} for x in df.columns]),
        html.P('Insert Y axis data'),
        dcc.Dropdown(id='yaxis-data',
                     options=[{'label':x,'value':x} for x in df.columns]),
        html.Button(id='submit-button', children='Create Graph'),
        html.Hr(),

        dash_table.DataTable(
            data=df.to_dict('rocords'),
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
        return dcc.Graph(figure=bar_fig), \
            html.Button(id='model-button', children='Modelliere Zeitreihe'),\
            html.Hr()


if __name__ == '__main__':
    app.run_server(debug=True)