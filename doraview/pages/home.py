import dash
import dash_mantine_components as dmc

from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')


dash.register_page(__name__, path='/', name='Home', order=0)

layout = dmc.Container([

	# Container for tutorial content
	dmc.Container(
		[
			dmc.Title("Welcome to Home Page", order=1),

			dmc.Select(
				label="Select country of of interest",
				placeholder="Select a country",
				id="dropdown-selection",
				value="Canada",
				data=df.country.unique()
			),
			dcc.Graph(id='graph-content')
		]
	),

	# Container for new app Home content
	dmc.Container(
		[
			dmc.Title("DORA Dashboard", order=1),

			# Stack to create two layers for two Groups. These will each have two of the DORA metic figures with all apps shown.
			# https://www.dash-mantine-components.com/components/stack
			dmc.Stack(
				[
					# Two groups to contain two each of the DORA metric figures
					# https://www.dash-mantine-components.com/components/group
					dmc.Group(
						# props as configured above:
						justify="center",
						gap="md",
						grow=True,
						# other props...
						children=[
							dmc.Button("A button", variant="default"),
							dmc.Button("A button", variant="default"),
						]
					),
						dmc.Group(
						# props as configured above:
						justify="center",
						gap="md",
						grow=True,
						# other props...
						children=[
							dmc.Button("A button", variant="default"),
							dmc.Button("A button", variant="default"),
						]
					),
				]
			),
		]
	),

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