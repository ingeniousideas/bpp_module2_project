# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
import dash_ag_grid as dag

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash()

# App layout
app.layout = dmc.MantineProvider(

    dmc.Container([
        dmc.Title("My First App with Data, Graph, and Controls", c="blue", order=3), # order is size of text

        dmc.RadioGroup(
           dmc.Group([dmc.Radio(i, value=i) for i in  ['pop', 'lifeExp', 'gdpPercap']]), # callback input component
            id='my-dmc-radio-item',
            value='lifeExp',
            p="sm"
        ),

        dmc.SimpleGrid([
            dag.AgGrid(
                rowData=df.to_dict("records"),
                columnDefs=[{"field": i} for i in df.columns],
            ),

            dcc.Graph(figure={}, id='graph-placeholder') # callback output reviever. Empty dictionary/graph.
        ], cols={"base": 1, "md": 2}) # type: ignore
    ], fluid=True)
)

# Add controls to build the interaction. The @callback is a decorator to the update_graph() function.
@callback(
    Output(component_id='graph-placeholder', component_property='figure')
    ,Input(component_id='my-dmc-radio-item', component_property='value')
)
def update_graph(col_chosen): # Takes the Input component_property value as y-axis attribute.
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig # outputs the graph object for the dcc.Graph(figure={}) dictionary.

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
