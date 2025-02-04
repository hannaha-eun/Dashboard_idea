import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import Dash, _dash_renderer, Input, Output, State, callback, clientside_callback
_dash_renderer._set_react_version("18.2.0")

layout = dmc.Container(
    [
        dmc.Title("Menu 3", order=2),
        dmc.Text("This is the content for Menu 3."),
    ],
    style={"padding": "20px"}
)
