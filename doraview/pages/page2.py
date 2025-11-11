import dash
from dash import html

dash.register_page(__name__, name='Page 2')

layout = html.Div([
    html.H1("This is Page 2")
])