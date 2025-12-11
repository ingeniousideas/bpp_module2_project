import dash
from dash import html
import pandas as pd

from components.table import reuse_table

dash.register_page(__name__, path='/failures', name='Failure Rate', order=4)

df_apps = pd.read_json('/home/lnx_workspaces/bpp_projects/bpp_module2_project/doraview/data/json/change_fail.json')

layout = html.Div([
    html.H1("Change Failure Rate"),
	reuse_table(df_apps, "Table of Deployment Failures")
])