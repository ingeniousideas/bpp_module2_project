# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='My First App with Data, Graph, and Controls')
    ,html.Hr()
    ,dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item') # callback input component
    ,dash_table.DataTable(data=df.to_dict('records'), page_size=6) # type: ignore
    ,dcc.Graph(figure={}, id='controls-and-graph') # callback output reviever. Empty dictionary/graph.
]

# Add controls to build the interaction. The @callback is a decorator to the update_graph() function.
@callback(
    Output(component_id='controls-and-graph', component_property='figure')
    ,Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen): # Takes the Input component_property value as y-axis attribute.
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig # outputs the graph object for the dcc.Graph(figure={}) dictionary.

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
