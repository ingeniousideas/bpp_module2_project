import dash
from dash import html
import pandas as pd

from components.table import reuse_table

dash.register_page(__name__, path='/lead_time', name='Lead Time for Changes', order=3)

df_apps = pd.read_json('/home/lnx_workspaces/bpp_projects/bpp_module2_project/doraview/data/json/change_lead_time.json')

layout = html.Div([
    html.H1("Lead Time for Changes"),
	reuse_table(df_apps, "Table of Commits and Lead Times")
])