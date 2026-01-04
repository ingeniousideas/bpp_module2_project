# Framework components
import dash
import pandas as pd
import dash_mantine_components as dmc
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

# Custom components
from components.table import reuse_table
from components.get_dataframes import figure_dataframe, raw_dataframe

dash.register_page(__name__, path='/restoration', name='Time to Restore', order=5)

df_incidents_basic = raw_dataframe('incidents')

layout = dmc.Container([

	# Page title.
	dmc.Title("Time to Restore Service"),

	dmc.Container(
		[
			# Smaller title for the figure, order=3 gives size of font.
			dmc.Title("Monthly  Observed Incidents", order=3),

			# Dropdown to select the data.
			dmc.Select(
				label="Select app",
				placeholder="Select app",
				id="incidents-dropdown-selection",
				value=df_incidents_basic.application_id.unique()[0],
				data=df_incidents_basic.application_id.unique()
			),

			# scatter chart with ema line
			dcc.Graph(id='incidents-scatter-graph'),

			# Filtered table callback output.
			html.Div(id='incidents-table-content'),
		]
	),
])

# Callback function to return a figure as defined by the dropdown.
@callback(
		Output('incidents-scatter-graph', 'figure'),
		Input('incidents-dropdown-selection', 'value')
	)
def update_mttr_graph(value):

	# Specify filtered data frame
	df_apps = df_incidents_basic.loc[df_incidents_basic.application_id==value].copy()
	df_apps.sort_values(by=["started_at"], inplace=True)

	# https://stackoverflow.com/questions/74520782/plotly-express-overlay-two-line-graphs
	fig_mttr_scat_trace = px.scatter(
		data_frame=df_apps,
		title="Lead Time for Changes Scatter Plot",	# Label for the figure.
		x="started_at",							# Column for use on x-axis
		y="duration_hours",							# Column for use on y-axis
		color="application_id",					# Column for use on color grouping
		trendline="ols",						# Add a trendline
		)

	fig_mttr_scat_trace.update_yaxes(
		title_text="Resolution Time (hours)"
	)
	
	fig_mttr_scat_trace.update_xaxes(
		title_text="Incident Date"
	)
	
	fig_mttr_scat_trace.update_layout(
		legend_title_text="Legend"
	)

	# Manually set colors from the plotly_dark palette
	# Assuming trace order: [0] scatter points, [1] trendline, [2] EMA
	fig_mttr_scat_trace.data[0].marker.color = '#636efa'  # Scatter points
	fig_mttr_scat_trace.data[1].line.color = '#ef553b'    # Trendline

	# Customize legend labels
	fig_mttr_scat_trace.data[0].name = f'Resolution Times'  # Scatter points

	# Apply Plotly colour pallet
	fig_mttr_scat_trace.update_layout(template="plotly_dark")

	return fig_mttr_scat_trace

@callback(
		Output('incidents-table-content', 'children'),
		Input('incidents-dropdown-selection', 'value')
)
def update_table(value):

	df_single_app = df_incidents_basic.loc[df_incidents_basic.application_id==value].copy()

	return reuse_table(df_single_app, "Table of Observed Incidents")