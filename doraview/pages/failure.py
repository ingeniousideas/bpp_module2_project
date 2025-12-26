import dash
import dash_mantine_components as dmc
import pandas as pd

from components.table import reuse_table

dash.register_page(__name__, path='/failures', name='Failure Rate', order=4)

raw_file_path = '/home/lnx_workspaces/bpp_projects/bpp_module2_project/doraview/data/json/change_fail.json'
df_apps = pd.read_json(raw_file_path, encoding='utf-8', convert_dates=["detected_at"])

layout = dmc.Container([
    dmc.Title("Change Failure Rate"),
	reuse_table(df_apps, "Table of Deployment Failures")
])