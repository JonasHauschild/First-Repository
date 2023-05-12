import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

Forecast = html.Div([
    html.Div(
        [dbc.Button('Predict',
                    id='Predict_id',
                    className='mb-3',
                    color='primayr'),
         html.Div(
             id='output-predict'),
         ], style={'padding': 10}
    )
])