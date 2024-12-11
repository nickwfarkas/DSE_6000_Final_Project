from callbacks.register_callbacks import register_callbacks
from layouts.layout import layout
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# dataset
df = pd.read_csv('./static/IEA-EV-dataEV-salesHistoricalCars.csv')
df['year'] = pd.to_datetime(df['year'], format='%Y')
df = df.dropna()

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "EV Trends Dashboard"

# App layout
app.layout = layout(df)

register_callbacks(app, df)

if __name__ == "__main__":
    app.run_server(debug=True)
