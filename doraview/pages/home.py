import dash
import dash_mantine_components as dmc

dash.register_page(__name__, path='/', name='Home', order=0)

layout = dmc.Container([
    dmc.Title("Welcome to Home Page")
])