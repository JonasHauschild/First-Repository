from dash import dcc
from dash import html

upload_box = html.Div([
    html.Label('Step 1'),
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
    html.Div(id='output-div'),  # tied to the second callback
    html.Div(id='output-datatable'),  # will hold return from first callback
    html.Div(id='output-modeldata'),  # will hold the modelled data
    dcc.Store(id='stored-data', data=None),
    dcc.Store(id='stored-data-1', data=None),
    html.P('Choose X-Axis'),
    dcc.Dropdown(id='xaxis-data', options={}),
    html.P('Choose Y-Axis'),
    dcc.Dropdown(id='yaxis-data', options={})
])