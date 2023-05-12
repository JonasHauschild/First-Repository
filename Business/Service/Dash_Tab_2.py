import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


# Plot Zeitreihe
_mygraph_time_series = dcc.Graph(figure={
    'data': [
        {'x': [1,2,3], 'y': [4,1,2], 'type': 'line'},
    ],
    'layout': {
        'title': 'My Dash Graph',
        'height': 400},
    }, style={'border': '1px solid'}
)

# Erklärung zur Interpretation der Teststatistik (Text)
mytext_explain_test= dcc.Markdown(children='Hier steht die Erklärung der Statistik')
mytext_interpret_test= dcc.Markdown(children='Hier steht die Ergebnisinterpretation der Statistik')


statistical_analysis = html.Div([
    dbc.Col([

        html.Div(

            [dbc.Button('Saisonalität',
                       id = 'collapse-button-saisonalität',
                       className= 'mb-3',
                       color= 'primary'),

                dbc.Collapse(
                    dbc.Row([
                        dbc.Col([
                            dbc.Card(
                                dbc.CardBody(

                                    children=[

                                        html.Label('Zeitreihe auf Saisonalität überprüfen'),
                                        html.Div(
                                            html.Button(
                                                id='submit-button-fft',
                                                children='Fast Fourier Test'
                                            )
                                        ),
                                        html.Br(),
                                        html.Label('Saisonalität bereinigen'),
                                        html.Div(
                                            html.Button(
                                                id='submit-button-sb',
                                                children='Saisonalität bereinigen'
                                            )
                                        ),
                                        html.Br(),
                                    ], style={'padding': 10, 'height': 500, 'flex': 1, 'border': '1px solid'}
                                )
                            ),
                        ]),
                        dbc.Col([
                            html.Div(
                                children=[
                                    _mygraph_time_series
                                ]
                            )
                        ]),
                    ]),
                    id = 'collapse-saisonalität', is_open=False),

                html.Div(
                    id='output-fft'
                ),
                html.Div(
                    id='output-sb'
                )
            ], style={'padding': 10}
        ),

        html.Br(),

        html.Div(

            [dbc.Button('Stationarität',
                        id='collapse-button-stationarität',
                        className='mb-3',
                        color='primary'),

             dbc.Collapse(
                 dbc.Row([
                     dbc.Col([
                         dbc.Card(
                             dbc.CardBody(

                                 children=[

                                     html.Label('Zeitreihe auf Stationarität überprüfen'),
                                     html.Div(
                                         html.Button(
                                             id='submit-button-adf',
                                             children='Augmented Dickey-Fuller Test'
                                         )
                                     ),

                                     html.Br(),

                                 ], style={'padding': 10, 'height': 500, 'flex': 1, 'border': '1px solid'}
                             )
                         ),
                     ]),
                     dbc.Col([
                         html.Div(
                             children=[
                                 _mygraph_time_series
                             ]
                         )
                     ]),
                 ]),
                 id='collapse-stationarität', is_open=False
             ),

             html.Div(
                 id='output-adf'
             )
            ], style={'padding': 10}
        ),

        html.Br(),

        html.Div(

            [dbc.Button('Residualverteilung',
                        id='collapse-button-autokorrelation der residualverteilung',
                        className='mb-3',
                        color='primary'),

             dbc.Collapse(
                 dbc.Row([
                     dbc.Col([
                         dbc.Card(
                             dbc.CardBody(

                                 children=[

                                     html.Label('Autokorrelation der Residualverteilung testen'),
                                     html.Div(
                                         html.Button(
                                             id='submit-button-ak',
                                             children='Test starten'
                                         )
                                     ),

                                     html.Br(),

                                 ], style={'padding': 10, 'height': 500, 'flex': 1, 'border': '1px solid'}
                             )
                         ),
                     ]),
                     dbc.Col([
                         html.Div(
                             children=[
                                 _mygraph_time_series
                             ]
                         )
                     ]),
                 ]),
                 id='collapse-autokorrelation', is_open=False
             ),

             html.Div(
                 id='output-ak'
             )
             ], style={'padding': 10}
        ),

        html.Br(),


        html.Div(

            [dbc.Button('Modellierung',
                        id='collapse-button-modell',
                        className='mb-3',
                        color='primary'),
             dbc.Collapse(
                 dbc.Card(
                     dbc.CardBody(
                         children=[

                             html.Label('Parameter für die Modellierung der Saisonalität wählen'),

                             dbc.Col([
                                 'Parameter p: ',
                                 dcc.Input(
                                     id='input-circular-1-saison', type='number', min=0, max=20, value=2
                                 ),
                                 'Parameter d: ',
                                 dcc.Input(
                                     id='input-circular-2-saison', type='number', min=0, max=20, value=1
                                 ),
                                 'Parameter q: ',
                                 dcc.Input(
                                     id='input-circular-3-saison', type='number', min=0, max=20, value=0
                                 ),
                                 'Parameter s: ',
                                 dcc.Input(
                                     id='input-circular-4-saison', type='number', min=0, max=31, value=23
                                 )
                             ]),

                             html.Br(),

                             html.Label('Gwählte Parameter für die Modellierung der Saisonalität anwenden'),

                             html.Br(),

                             html.Label('Parameter für das Arima-Modell wählen'),

                             dbc.Col([
                                 'Parameter p: ',
                                 dcc.Input(
                                     id='input-circular-1-arima', type='number', min=0, max=20, value=1
                                 ),
                                 'Parameter d: ',
                                 dcc.Input(
                                     id='input-circular-2-arima', type='number', min=0, max=20, value=1
                                 ),
                                 'Parameter q: ',
                                 dcc.Input(
                                     id='input-circular-3-arima', type='number', min=0, max=20, value=0
                                 )
                             ]),

                             html.Br(),

                             html.Label('Gwählte Parameter für die Arima-Modellierung anwenden'),

                             html.Br(),

                             html.Label('Parameter für die exogenen Faktoren wählen'),

                             dbc.Col([
                                 'Parameter x: ',
                                 dcc.Input(
                                     id='input-circular-exo-arima', type='number', min=0, max=20, value=0
                                 )
                             ]),

                             html.Br(),

                             html.Label('Gwählte Parameter für die exogenen Faktoren der Saisonalität anwenden'),

                             html.Br(),

                             html.Label('Modellierung durchführen'),

                             html.Div(
                                 html.Button(
                                     id='submit-button-modell',
                                     children='Sarimax-Modell anwenden'
                                 )
                             ),

                             html.Br(),


                         ], style={'padding': 10, 'flex': 1, 'border': '1px solid'}
                     )
                 ),
                 id='collapse-modell', is_opem=False
             ),

            html.Div(
                id='output-forecast-mean'),
             html.Div(
                id='output-fitted-timeseries'),
             html.Div(
                id='output-forecast-quantile'),
             html.Div(
                id='results')
            ], style={'padding': 10}

        )
    ])
], style= {'display': 'flex', 'flex-direction': 'row'})