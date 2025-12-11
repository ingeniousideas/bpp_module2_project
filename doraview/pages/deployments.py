import dash
from dash import html
import pandas as pd

from components.table import reuse_table

dash.register_page(__name__, path='/deployments', name='Deployment Frequency', order=2)

df_apps = pd.read_json('/home/lnx_workspaces/bpp_projects/bpp_module2_project/doraview/data/json/deployment_frequency.json')

layout = html.Div([
	html.H1("Deployment Frequency"),
	reuse_table(df_apps, "Table of Application Feature Deployments")
])