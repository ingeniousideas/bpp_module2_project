import dash
import pandas as pd
import dash_mantine_components as dmc
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

from components.table import reuse_table

dash.register_page(__name__, path='/restoration', name='Time to Restore', order=5)

df_apps = pd.read_json('/home/lnx_workspaces/bpp_projects/bpp_module2_project/doraview/data/json/incidents.json')
df_graph = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

layout = dmc.Container([

	# Page title.
	dmc.Title("Time to Restore Service"),

	# Data displayed as figure.
	dmc.Container(
		[
			# Smaller title for the figure, order=3 gives size of font.
			dmc.Title("Table of Observed Incidents", order=3),

			# Dropdown to select the data.
			dmc.Select(
				label="Select country of of interest",
				placeholder="Select a country",
				id="incidents-dropdown-selection",
				value="Canada",
				data=df_graph.country.unique()
			),
			dcc.Graph(id='incidents-graph-content')
		]
	),

	# Data displayed in table.
	reuse_table(df_apps, "Table of Observed Incidents"),

])

# Callback function to return a figure as defined by the dropdown.
@callback(
Output('incidents-graph-content', 'figure'),
Input('incidents-dropdown-selection', 'value')
)
def update_graph(value):

	# Specify filtered data frame
	dff = df_graph[df_graph.country==value]

	# Specify figure attributes and characteristics
	fig = px.line(dff, x='year', y='pop')

	# Apply Plotly colour pallet
	fig.update_layout(template="plotly_dark")

	return fig