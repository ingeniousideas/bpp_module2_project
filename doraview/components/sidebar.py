import dash
from dash import Dash, html, dash_table

import dash_bootstrap_components as dbc

def reuse_sidebar():

	return html.Div(
		[
			html.H2("Pages", className="sidebar-header"),

			html.Hr(),

			# Dynamically create links for each page
			dbc.Nav(
				[
					dbc.NavLink(
						page["name"], href=page["path"], active="exact"
					) for page in dash.page_registry.values()
				],
				vertical=True,
				pills=True,
			),
		],
		className="sidebar",
	)