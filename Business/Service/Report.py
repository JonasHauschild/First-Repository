
import dash
from dash import Dash, html
from dash import dash_table
from dash import dcc
import plotly.graph_objects as go
import pandas as pd

# Beispiel-Daten
dateipfad = r'C:\Users\jonas.hauschild\PycharmProjects\First-Repository-2\Business\Test-Data\report_data.xlsx'

df = pd.read_excel(dateipfad, sheet_name='Report_Data', header=0, engine='openpyxl')

# Zeiträume aus der ersten Zeile extrahieren
perioden = df.iloc[0, 1:7].tolist()


# Funktion zur Extraktion der Werte für eine Kennzahl

def find_row(label):
    for i in range(len(df)):
        if isinstance(df.iloc[i, 0], str) and label in df.iloc[i, 0]:
            return df.iloc[i, 1:].astype(float).tolist()
    return []

# Werte extrahieren
cbc_values = find_row("CBC")
fce_values = find_row("FCE")
lue_values = find_row("LÜ")



# Diagramm erstellen
fig = go.Figure()
fig.add_trace(go.Scatter(x=perioden, y=cbc_values, mode='lines+markers', name='CBC', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=perioden, y=fce_values, mode='lines+markers', name='FCE', line=dict(color='green')))
fig.add_trace(go.Scatter(x=perioden, y=fce_values, mode='lines+markers', name='LÜ', line=dict(color='red')))

fig.update_layout(
    title='Entwicklung der Kennzahlen (CBC, FCE, LÜ)',
    xaxis_title='Periode',
    yaxis_title='Wert',
    plot_bgcolor='rgba(240,240,240,0.95)',
    paper_bgcolor='rgba(255,255,255,1)',
    font=dict(family='Arial', size=12),
    legend=dict(orientation='h', y=-0.2)
)

# Dash-App initialisieren
app = Dash(__name__)

# Layout definieren
app.layout = html.Div(style={'backgroundColor': '#f9f9f9', 'padding': '20px'},
                      children=[
                          html.H1("Liquiditätsreport", style={'textAlign': 'center', 'color': '#333'}),
                          html.Div([
                              dash_table.DataTable(data=df.to_dict('records'),
                                                   columns=[{"name": i, "id": i} for i in df.columns],
                                                   style_table={'overflowX': 'auto'},
                                                   style_cell={'textAlign': 'left'},
                                                   page_size=100)
                          ]),
                          html.Div([dcc.Graph(figure=fig)], style={'margin': 'auto', 'width': '80%'})
])

if __name__ == '__main__':
    app.run(debug=True)


