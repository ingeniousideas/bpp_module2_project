import dash
import dash_mantine_components as dmc
import pandas as pd

from components.table import reuse_table

dash.register_page(__name__, path='/apps', name='Applications', order=1)

df_apps = pd.read_json('/home/lnx_workspaces/bpp_projects/bpp_module2_project/doraview/data/json/applications.json')

layout = dmc.Container([
	dmc.Title("Applications"),
	reuse_table(df_apps, "Table of Applications")
	],
	fluid=True,
	p="md"
)