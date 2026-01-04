import dash
import pandas as pd
import dash_mantine_components as dmc
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

from components.table import reuse_table

dash.register_page(__name__, path='/restoration', name='Time to Restore', order=5)

raw_file_path = '/home/lnx_workspaces/bpp_projects/bpp_module2_project/doraview/data/json/incidents.json'

df_incidents_raw  = pd.read_json(
	raw_file_path,
	encoding='utf-8',
	convert_dates=["incident_start_time", "incident_end_time"]
	)

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
				value=df_incidents_raw.application_id.unique()[0],
				data=df_incidents_raw.application_id.unique()
			),

			# scatter chart with ema line
			dcc.Graph(id='incidents-scatter-graph'),

			# Data displayed in table.
			reuse_table(df_incidents_raw, "Table of Observed Incidents"),

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
	df_apps = df_incidents_raw.loc[df_incidents_raw.application_id==value].copy()
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