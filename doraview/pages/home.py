import dash
import dash_mantine_components as dmc

from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')


dash.register_page(__name__, path='/', name='Home', order=0)

layout = dmc.Container([
    dmc.Title("Welcome to Home Page"),
	
	dmc.Select(
		label="Select country of of interest",
		placeholder="Select a country",
		id="dropdown-selection",
		value="Canada",
		data=df.country.unique()
	),
	dcc.Graph(id='graph-content')
])

@callback(
	Output('graph-content', 'figure'),
	Input('dropdown-selection', 'value')
)
def update_graph(value):
	dff = df[df.country==value]
	fig = px.line(dff, x='year', y='pop')
	fig.update_layout(template="plotly_dark")
	return fig