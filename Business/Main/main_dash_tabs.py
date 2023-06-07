import base64
import datetime
import pandas as pd
import io
import plotly.express as px
import numpy as np

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table

from Business.Service.ServiceStatisticTools import ServiceStatisticTools
from Business.Service.ServiceModellSarimax import ServiceModellSarimax # oder Business als Source Root markieren und nur Service... schreiben

from statsmodels.tsa.stattools import acf, pacf

from Business.Service.Dash_Tab_1 import upload_box
from Business.Service.Dash_Tab_2 import statistical_analysis
from Business.Service.Dash_Tab_3 import Forecast

external_stylesheets = [dbc.themes.LUMEN] #Choose any theme you like on the website of dbc

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                suppress_callback_exceptions=True)

app.layout = html.Div([ # this code section taken from Dash docs https://dash.plotly.com/dash-core-components/upload
    html.H1('Einlagenmodellierung'),
    dcc.Tabs([
        dcc.Tab(label='Input and View Data', children=[
            upload_box
        ]),
        dcc.Tab(label='Statistical Analysis and Model Parameters', children=[
            statistical_analysis
        ]),
        dcc.Tab(label='Forecasting', children=[
            Forecast
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
        html.P('Choose X-Axis'),
        dcc.Dropdown(id='xaxis-data',
                     options=[{'label':x,'value':x} for x in df.columns]),
        html.P('Choose Y-Axis'),
        dcc.Dropdown(id='yaxis-data',
                     options=[{'label':x,'value':x} for x in df.columns]),
        html.Button(id='submit-button', children='Create Graph'),
        html.Hr(),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
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
        return dcc.Graph(figure=bar_fig)


@app.callback(Output('output-fft', 'children'),
              Input('submit-button-fft', 'n_clicks'))
def test_fft(n):
    if n is None:
        return dash.no_update
    else:
        #plot plotten
        print(n)


@app.callback(Output('output-sb', 'children'),
              Input('submit-button-sb', 'n_clicks'))
def test_sb(n):
    if n is None:
        return dash.no_update
    else:
        #plot plotten
        print(n)


@app.callback(Output('output-adf', 'children'),
              Input('submit-button-adf', 'n_clicks'),
              State('stored-data', 'data'))
def test_adf(n, data):
    if n is None:
        return dash.no_update
    else:
        data_df = pd.DataFrame.from_dict(data)
        df_stats = pd.DataFrame.from_dict(ServiceStatisticTools.run_adf(data=data_df['Amount_EUR']))
        df_stats = df_stats.rename_axis('Alpha').reset_index()

        card = dbc.Card(
            [
                html.Div(dash_table.DataTable(df_stats.to_dict('records'), [{"name": i, "id": i} for i in df_stats.columns]))
            ], style={"width": "18rem"},
        )

        return card


@app.callback(Output('output-acf', 'figure'),
              Input('submit-button-acf', 'n_clicks'),
              State('stored-data', 'data'))
def test_ak(n, data):
    if n is None:
        return dash.no_update
    else:
        data_df = pd.DataFrame.from_dict(data)
        df_acf = acf(data_df['Amount_EUR'], nlags=10)
        df_acf = pd.DataFrame(df_acf, columns=['ACF'])
        df_acf['LAG']=df_acf.index
        fig = px.scatter(df_acf, x='LAG', y='ACF')

        return fig


@app.callback(Output('output-pacf', 'figure'),
              Input('submit-button-pacf', 'n_clicks'),
              State('stored-data', 'data'))
def test_ak(n, data):
    if n is None:
        return dash.no_update
    else:
        data_df = pd.DataFrame.from_dict(data)
        df_pacf = pacf(data_df['Amount_EUR'], nlags=10)
        df_pacf = pd.DataFrame(df_pacf, columns=['PACF'])
        df_pacf['LAG'] = df_pacf.index
        fig = px.scatter(df_pacf, x='LAG', y='PACF')

        return fig


@app.callback(Output('output-button-params-saison', 'children'),
              Input('submit-button-params-saison', 'n_clicks'),
              State('input-circular-1-saison', 'value'),
              State('input-circular-2-saison', 'value'),
              State('input-circular-3-saison', 'value'),
              State('input-circular-4-saison', 'value'))
def button_params_saison(n, value1, value2, value3, value4):
    if n is None:
        return dash.no_update
    else:
        # Funktion Saison hier einfügen
        print('button Saison', value1, value2, value3, value4)


@app.callback(Output('output-button-params-arima', 'children'),
              Input('submit-button-params-arima', 'n_clicks'),
              State('input-circular-1-arima', 'value'),
              State('input-circular-2-arima', 'value'),
              State('input-circular-3-arima', 'value'))
def button_params_arima(n, value1, value2, value3):
    if n is None:
        return dash.no_update
    else:
        #Funktion Arimax hier einfügen
        print('button Arima', value1, value2, value3)


@app.callback(Output('output-button-params-exogen', 'children'),
              Input('submit-button-params-exogen', 'n_clicks'),
              State('input-circular-exo-arima', 'value'))
def exogen(n, value):
    if n is None:
        return dash.no_update
    else:
        #Funktion Arimax hier einfügen
        print('button Exogen', value)


@app.callback(Output('results', 'children'),
              Input('submit-button-modell', 'n_clicks'),
              State('input-circular-1-saison', 'value'),
              State('input-circular-2-saison', 'value'),
              State('input-circular-3-saison', 'value'),
              State('input-circular-4-saison', 'value'),
              State('input-circular-1-arima', 'value'),
              State('input-circular-2-arima', 'value'),
              State('input-circular-3-arima', 'value'),
              State('stored-data', 'data'),
              State('xaxis-data', 'value'),
              State('yaxis-data', 'value'))
def button_modell(n, season_p, season_d, season_q, season_s, arima_p, arima_d, arima_q, df, xaxis, yaxis):
    if n is None:
        return dash.no_update
    else:
        print('Modell Button')
        print('Seasonal Order: {}'.format((season_p, season_d, season_q, season_s)))
        print('Arima Order: {}'.format((arima_p, arima_d, arima_q)))
        fit, forecast, results = ServiceModellSarimax(data=pd.DataFrame(df),
                                                      xcol=xaxis,
                                                      ycol=yaxis,
                                                      order=(arima_p, arima_d, arima_q),
                                                      seasonal_order=(season_p, season_d, season_q, season_s)).run()

        fitted_timeseries = fit.predict()
        fitted_timeseries = fitted_timeseries.iloc[1:]
        forecast_mean = forecast.predicted_mean
        forecast_quantile = forecast.conf_int(alpha=0.01)
        #Feedbackbox eingeben "Fertig"

        return html.Div([dcc.Store(id='stored-data-1', data=results.to_dict('records'))])


@app.callback(Output('collapse-saisonalität', 'is_open'),
              [Input('collapse-button-saisonalität', 'n_clicks')],
              [State('collapse-saisonalität', 'is_open')])
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(Output('collapse-stationarität', 'is_open'),
              [Input('collapse-button-stationarität', 'n_clicks')],
              [State('collapse-stationarität', 'is_open')])
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(Output('collapse-autokorrelation', 'is_open'),
              [Input('collapse-button-autokorrelation', 'n_clicks')],
              [State('collapse-autokorrelation', 'is_open')])
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(Output('collapse-modell', 'is_open'),
              [Input('collapse-button-modell', 'n_clicks')],
              [State('collapse-modell', 'is_open')])
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(Output('output-predict', 'children'),
              Input('Predict_id', 'n_clicks'),
              State('stored-data-1', 'data'))
def make_Forecast_plot(n, results):
    if n is None:
        return dash.no_update
    else:
        fig = px.line(results, x='Hist_Date', y=['Historie', 'Mittelwert']) #'0.99-Quantil lower', '0.99-Quantil upper'

        return dcc.Graph(figure=fig)


if __name__ == '__main__':
    app.run_server(debug=True)