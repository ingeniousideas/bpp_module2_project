import dash
import dash_mantine_components as dmc
from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

from components.table import reuse_table

dash.register_page(__name__, path='/failures', name='Failure Rate', order=4)

fail_raw_file_path = '/home/lnx_workspaces/bpp_projects/bpp_module2_project/doraview/data/json/change_fail.json'
df_fail = pd.read_json(fail_raw_file_path, encoding='utf-8', convert_dates=["detected_at"])

deploy_raw_file_path = '/home/lnx_workspaces/bpp_projects/bpp_module2_project/doraview/data/json/deployment_frequency.json'
df_deploy_raw = pd.read_json(deploy_raw_file_path, encoding='utf-8', convert_dates=["deployed_at"])


"""  Update dtaftame for use by the graph callback

	Reduce the number of columns for simplicity.
	Add new grouping column "month.
"""
# Reduce number of columns
df_deploy_graph = df_deploy_raw[["application_id","application_name","environment","status","deployed_at"]].copy()
# Add Month column for grouping.
df_deploy_graph["month"] = df_deploy_graph["deployed_at"].dt.month

# create grouped data frame
df_deploy_graph_groupby = df_deploy_graph.groupby([
	"application_id",
	"application_name",
	"month",
	"environment",
	"status"
	])["month"].count().reset_index(name="count")

layout = dmc.Container([

	# Page title.
	dmc.Title("Change Failure Rate"),

	dmc.Container(
		[
			# Smaller title for the figure, order=3 gives size of font.
			dmc.Title("Deployment Failures Over Time", order=3),

			# Dropdown to select the data.
			dmc.Select(
				label="Select app",
				placeholder="Select app",
				id="failure-dropdown-selection",
				value="app001",
				data=df_deploy_graph_groupby.application_id.unique()
			),

			# Graph to show deployment failure data.
			dcc.Graph(id='failure-graph-content',
				
			),
		]
	),
	reuse_table(df_fail, "Table of Deployment Failures")
])

# Callback function to return a figure as defined by the dropdown.
@callback(
Output('failure-graph-content', 'figure'),
Input('failure-dropdown-selection', 'value')
)
def update_graph(value):

	# Specify filtered data frame
	df_deploy_graph = df_deploy_graph_groupby[df_deploy_graph_groupby.application_id==value]

	deploy_fig = px.bar(
		df_deploy_graph,
		title="Monthly Deployments by Application",
		x='month',
		y='count',
		color='status',
		color_discrete_map={
			"success":"#636EFA",
			"failed":"#EF553B"
			},
		category_orders={
			"status":[
				"success",
				"failed"
				]},
		facet_col='application_id'
	)

	deploy_fig.update_xaxes(
		title_text="Deployment Month",
		tickvals=list(range(1,13)),
		ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	)

	# Apply Plotly colour pallet
	deploy_fig.update_layout(template="plotly_dark")

	return deploy_fig
