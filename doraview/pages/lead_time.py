import dash
import dash_mantine_components as dmc
from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

from components.table import reuse_table

dash.register_page(__name__, path='/lead_time', name='Lead Time for Changes', order=3)

df_apps = pd.read_json('/home/lnx_workspaces/bpp_projects/bpp_module2_project/doraview/data/json/change_lead_time.json')

layout = dmc.Container([
    dmc.Title("Lead Time for Changes"),
	reuse_table(df_apps, "Table of Commits and Lead Times")
])