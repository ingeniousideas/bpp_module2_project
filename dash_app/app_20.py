# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
import dash_ag_grid as dag

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

df_apps = pd.read_json('/home/lnx_workspaces/bpp_projects/bpp_module2_project/dash_app/data/json/applications.json')

df_deploy = pd.read_json('/home/lnx_workspaces/bpp_projects/bpp_module2_project/dash_app/data/json/deployments.json')

df_failure = pd.read_json('/home/lnx_workspaces/bpp_projects/bpp_module2_project/dash_app/data/json/failures.json')

df_incident = pd.read_json('/home/lnx_workspaces/bpp_projects/bpp_module2_project/dash_app/data/json/incidents.json')

df_lead = pd.read_json('/home/lnx_workspaces/bpp_projects/bpp_module2_project/dash_app/data/json/lead_times.json')

# Initialize the app
app = Dash()

style = {
    "height": 100,
    "border": f"1px solid {dmc.DEFAULT_THEME['colors']['indigo'][4]}",
    "marginTop": 20,
    "marginBottom": 20,
}

grid = {
    "border": f"1px solid {dmc.DEFAULT_THEME['colors']['indigo'][4]}",
    "marginTop": 10,
    "marginBottom": 10,
}

# App layout
app.layout = dmc.MantineProvider(

    html.Div(
        children=[

		dmc.Container([
            dmc.Title("Tutorial App with Data, Graph, and Controls", c="blue", order=3), # order is size of text

            dmc.RadioGroup(
               dmc.Group([dmc.Radio(i, value=i) for i in  ['pop', 'lifeExp', 'gdpPercap']]), # callback input component
                id='my-dmc-radio-item',
                value='lifeExp',
                p="sm"
            ),

            # simple grid for the tutorial components
            dmc.SimpleGrid([

                # simple table for the data
                dag.AgGrid(
                    rowData=df.to_dict("records"),
                    columnDefs=[{"field": i} for i in df.columns],
                ),
    
                # histogram
                dcc.Graph(figure={}, id='graph-placeholder'), # callback output reciever. Empty dictionary/graph.

               # defines the grid size for the figure objects
            ], cols={"base": 1, "md": 2}, spacing={"base": 10, "sm": "xl"}, verticalSpacing={"base": "md", "sm": "xl"}), # type: ignore

		], fluid=True, style=grid),

		dmc.Container([
            dmc.Title("Application data", c="blue", order=3), # order is size of text

            # simple grid for the application components
            dmc.SimpleGrid([
		    
                # simple table for the application data
                dag.AgGrid(
                    rowData=df_apps.to_dict("records"),
                    columnDefs=[{"field": i} for i in df_apps.columns],
                ),
               # defines the grid size for the figure objects
            ], cols={"base": 1, "md": 2}, spacing={"base": 10, "sm": "xl"}, verticalSpacing={"base": "md", "sm": "xl"}), # type: ignore

		], fluid=True, style=grid),

		dmc.Container([
            dmc.Title("Deployment data", c="blue", order=3), # order is size of text

            # simple grid for the deployment components
            dmc.SimpleGrid([
                # simple table for the deployments data
                dag.AgGrid(
                    rowData=df_deploy.to_dict("records"),
                    columnDefs=[{"field": i} for i in df_deploy.columns],
                ),
               # defines the grid size for the figure objects
            ], cols={"base": 1, "md": 2}, spacing={"base": 10, "sm": "xl"}, verticalSpacing={"base": "md", "sm": "xl"}), # type: ignore

		], fluid=True, style=grid),

		dmc.Container([
            dmc.Title("Failure data", c="blue", order=3), # order is size of text

            # simple grid for the failure components
            dmc.SimpleGrid([
                # simple table for the failures data
                dag.AgGrid(
                    rowData=df_failure.to_dict("records"),
                    columnDefs=[{"field": i} for i in df_failure.columns],
                ),
               # defines the grid size for the figure objects
            ], cols={"base": 1, "md": 2}, spacing={"base": 10, "sm": "xl"}, verticalSpacing={"base": "md", "sm": "xl"}), # type: ignore

		], fluid=True, style=grid),

		dmc.Container([
            dmc.Title("Incidents data", c="blue", order=3), # order is size of text

            # simple grid for the incidents components
            dmc.SimpleGrid([
                # simple table for the incidents data
                dag.AgGrid(
                    rowData=df_incident.to_dict("records"),
                    columnDefs=[{"field": i} for i in df_incident.columns],
                ),
               # defines the grid size for the figure objects
            ], cols={"base": 1, "md": 2}, spacing={"base": 10, "sm": "xl"}, verticalSpacing={"base": "md", "sm": "xl"}), # type: ignore

		], fluid=True, style=grid),

		dmc.Container([
            dmc.Title("Lead Time data", c="blue", order=3), # order is size of text

            # simple grid for the lead time components
            dmc.SimpleGrid([
                # simple table for the lead times data
                dag.AgGrid(
                    rowData=df_lead.to_dict("records"),
                    columnDefs=[{"field": i} for i in df_lead.columns],
                ),
               # defines the grid size for the figure objects
            ], cols={"base": 1, "md": 2}, spacing={"base": 10, "sm": "xl"}, verticalSpacing={"base": "md", "sm": "xl"}) # type: ignore

		], fluid=True, style=grid),

	])
)

# Add controls to build the interaction. The @callback is a decorator to the update_graph() function.
@callback(
    Output(component_id='graph-placeholder', component_property='figure')
    ,Input(component_id='my-dmc-radio-item', component_property='value'))
def update_graph(col_chosen): # Takes the Input component_property value as y-axis attribute.
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig # outputs the graph object for the dcc.Graph(figure={}) dictionary.

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
