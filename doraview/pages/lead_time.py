import dash
import dash_mantine_components as dmc
from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

from components.table import reuse_table

dash.register_page(__name__, path='/lead_time', name='Lead Time for Changes', order=3)

raw_file_path = '/home/lnx_workspaces/bpp_projects/bpp_module2_project/doraview/data/json/change_lead_time.json'

df_lead_raw = pd.read_json(
	raw_file_path,
	encoding='utf-8',
	convert_dates=["committed_at", "deployed_at"]
	)

""" Update dataframe for use by the graph callback

	Add Exponential Moving Average (EMA) column for trend.
"""
# Add Exponential Moving Average (EMA) column
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ewm.html
df_lead_raw["EMA"] = df_lead_raw["lead_time_hours"].ewm(span=5, adjust=False).mean()

layout = dmc.Container([

	dmc.Container(
		[
			# Title for the page.
			dmc.Title("Lead Time for Changes", order=1),

			# Dropdown to select the data.
			dmc.Select(
				label="Select app",
				placeholder="Select app",
				id="lead-time-dropdown-selection",
				value=df_lead_raw.application_id.unique()[0],
				data=df_lead_raw.application_id.unique()
			),

			# Graph to show lead time data.
			dcc.Graph(id='lead-time-graph-content'),
			
			reuse_table(df_lead_raw, "Table of Commits and Lead Times")
		],
	)
])

# Callback function to return a figure as defined by the dropdown.
@callback(
Output('lead-time-graph-content', 'figure'),
Input('lead-time-dropdown-selection', 'value')
)
def update_graph(value):
	
	# Specify filtered data frame
	df_lead_graph = df_lead_raw[df_lead_raw.application_id==value]
	df_lead_graph.sort_values(by=["commit_time"], inplace=True)

	# https://stackoverflow.com/questions/74520782/plotly-express-overlay-two-line-graphs
	fig_lead_scat_trace = px.scatter(
		data_frame=df_lead_graph,
		title="Lead Time for Changes Scatter Plot",	# Label for the figure.
		x="commit_time",							# Column for use on x-axis
		y="lead_time_hours",							# Column for use on y-axis
		color="application_id",					# Column for use on color grouping
		trendline="ols",						# Add a trendline
		)


	fig_lead_ema_trace = px.line(
		data_frame=df_lead_graph,
		title="Lead Time for Changes with EMA Line Plot",	# Label for the figure.
		x="commit_time",							# Column for use on x-axis
		y="EMA",							# Column for use on y-axis
		color="application_id",					# Column for use on color grouping
		)

	# Combine the two figures
	fig_lead_scat_trace.add_traces(
		list(fig_lead_ema_trace.select_traces())
	)

	# Manually set colors from the plotly_dark palette
	# Assuming trace order: [0] scatter points, [1] trendline, [2] EMA
	fig_lead_scat_trace.data[0].marker.color = '#636efa'  # Scatter points
	fig_lead_scat_trace.data[1].line.color = '#ef553b'    # Trendline
	fig_lead_scat_trace.data[2].line.color = '#00cc96'    # EMA line

	# Customize legend labels
	fig_lead_scat_trace.data[0].name = 'Datapoints'
	fig_lead_scat_trace.data[1].name = 'Trendline'
	fig_lead_scat_trace.data[2].name = 'EMA'

	# Apply Plotly colour pallet
	fig_lead_scat_trace.update_layout(template="plotly_dark")

	return fig_lead_scat_trace
