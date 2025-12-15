import dash
import pandas as pd
import dash_mantine_components as dmc

from components.table import reuse_table

dash.register_page(__name__, path='/restoration', name='Time to Restore', order=5)

df_apps = pd.read_json('/home/lnx_workspaces/bpp_projects/bpp_module2_project/doraview/data/json/incidents.json')

layout = dmc.Container([
    dmc.Title("Time to Restore Service"),
	reuse_table(df_apps, "Table of Observed Incidents")
])