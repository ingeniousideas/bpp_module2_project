import dash
from dash import html

dash.register_page(__name__, path='/', name='Home')

layout = html.Div([
    html.H1("Welcome to Home Page")
])