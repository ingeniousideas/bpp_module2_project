import plotly.express as px

def fig_bar_multi(dataframe, view):

	if view == "deploy":

		df_fig_bar = dataframe

		title = "Total Monthly Deployments by Application"

		x_values = 'month'
		y_values = 'count'

		x_title = "Deployment Month"
		y_title = "Number of Deployments"

		bar_color = 'application_id'
		color_map = None

	elif view == "fail_graph":

		df_status_grouped = dataframe.groupby(['month', 'status']).agg({'status':'count'})

		df_status_percent = df_status_grouped.groupby(level=0).apply(
			lambda x: 100 * x / x.sum())

		# Fix the index (drop the duplicate month level)
		df_status_percent.index = df_status_percent.index.droplevel(1)

		# Rename the column to avoid conflict during reset_index
		df_status_percent = df_status_percent.rename(columns={'status':'percentage'})

		df_fig_bar = df_status_percent.reset_index()

		title = "Deployment Failure Rates by Month"

		x_values = 'month'
		y_values = 'percentage'

		x_title = "Failure Month"
		y_title = "Percentage (%) Outcomes"

		bar_color = "status"

		color_map = {
			"success":"#636EFA",
			"failed":"#EF553B"
			}

	fig_bar_multi = px.bar(
		data_frame=df_fig_bar,
		title=title,
		x=x_values,
		y=y_values,
		color=bar_color,
		color_discrete_map = color_map,
	)

	fig_bar_multi.update_layout(legend_title_text="Legend")
	fig_bar_multi.update_layout(barmode='stack')
	fig_bar_multi.update_yaxes(title_text=y_title)
	fig_bar_multi.update_xaxes(
		title_text=x_title,
		tickvals=list(range(1,13)),
		ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	)

	# Apply Plotly colour pallet
	fig_bar_multi.update_layout(template="plotly_dark")

	return fig_bar_multi

def fig_bar_single(dataframe, app_id, view):

	if view == "deploy":

		# Specify filtered data frame
		df_fig_bar = dataframe[dataframe.application_id==app_id]

		title = "Total Monthly Deployments by Application"

		x_values = 'month'
		y_values = 'count'

		x_title = "Deployment Month"
		y_title = "Number of Deployments"

		bar_color = None
		color_map = None

	elif view == "fail":

		# Filter deploy df to app id
		df_target = dataframe[dataframe['application_id']==app_id]

		df_status_grouped = df_target.groupby(['month', 'status']).agg({'status':'count'})

		df_status_percent = df_status_grouped.groupby(level=0).apply(
			lambda x: 100 * x / x.sum())

		# Fix the index (drop the duplicate month level)
		df_status_percent.index = df_status_percent.index.droplevel(1)

		# Rename the column to avoid conflict during reset_index
		df_status_percent = df_status_percent.rename(columns={'status':'percentage'})

		df_fig_bar = df_status_percent.reset_index()

		title = "Deployment Failure Rates by Month"

		x_values = 'month'
		y_values = 'percentage'

		x_title = "Failure Month"
		y_title = "Percentage (%) Outcomes"

		bar_color = "status"

		color_map = {
			"success":"#636EFA",
			"failed":"#EF553B"
			}

	fig_bar_single = px.bar(
		data_frame=df_fig_bar,
		title=title,
		x=x_values,
		y=y_values,
		color=bar_color,
		color_discrete_map = color_map,
	)

	fig_bar_single.update_layout(legend_title_text="Legend")
	fig_bar_single.update_layout(barmode='stack')
	fig_bar_single.update_yaxes(title_text=y_title)
	fig_bar_single.update_xaxes(
		title_text=x_title,
		tickvals=list(range(1,13)),
		ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	)

	# Apply Plotly colour pallet
	fig_bar_single.update_layout(template="plotly_dark")

	return fig_bar_single

def get_scatter_single():
	""" Return scatter figure for a single application id.

		Needed for:
			- Lead Time.
			- Time to Restore.

		This will require a parameter of the app_id.

		Optional Trendline and Moving Average plot.
	"""
	pass

def get_scatter_multi():
	""" Return scatter figure for all appliations.

		This will require a parameter of the app_id.

		Optional Trendline and Moving Average plot
	"""
	pass