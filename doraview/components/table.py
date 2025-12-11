from dash import Dash, html, dash_table, dcc, callback, Output, Input

import dash_ag_grid as dag
import dash_mantine_components as dmc

"""
	AGGrid component documentation: 			https://dash.plotly.com/dash-ag-grid
	For applying themes to AGGrid component: 	https://dash.plotly.com/dash-ag-grid/styling-themes
"""
ag_grid_themes = {
	1:"ag-theme-alpine",
	2:"ag-theme-alpine-dark",
	3:"ag-theme-alpine-auto-dark"
	}

grid_style = {"height": "200px", "width": "100%"}

def reuse_table(table_dataframe, table_title, ag_grid_theme=ag_grid_themes[3], grid_style=grid_style):

	return dmc.Container(

		[
		
		dmc.Title(table_title, order=3), # order is size of text
		# simple grid for the application components
		dmc.SimpleGrid([

			# simple table for the application data
			dag.AgGrid(
				rowData=table_dataframe.to_dict("records"),
				columnDefs=[{"field": i} for i in table_dataframe.columns],
				className=ag_grid_theme,
			),

		# defines the grid size for the figure objects
		],
		cols={"base": 1, "md": 2},
		spacing={"base": 10, "sm": "xl"},
		verticalSpacing={"base": "md", "sm": "xl"}), # type: ignore

	],
	fluid=True,
	style=grid_style)