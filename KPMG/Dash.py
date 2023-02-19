import dash
import pandas as pd
import plotly.express as px
from dash import html
from dash import dcc

df = pd.read_excel('./Price_Data.xlsx')

#Initialize the app
app = dash.Dash(__name__)

#Define the app layout
app.layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                    html.Div(className='four columns div-user-controls',
                             children=[
                                 html.H2('DASH - STOCK PRICES'),
                                 html.P('Visualising time series with Plotly - Dash.'),
                                 html.P('Pick one or more stocks from the dropdown below.')
                                ]
                             ),
                    html.Div(className='eight columns div-for-charts bg-grey',
                             children=[
                                 dcc.Graph(id='timeseries',
                                           config={'displayModeBar': False},
                                           animate=True,
                                           figure=px.line(df,
                                                          x='Date',
                                                          y='Apple',
                                                          template='plotly_dark').update_layout(
                                                                {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                                                 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
                                           ),
                                        ])
                            ])
            ]
        )

if __name__ == "__main__":
    app.run_server(debug=True)