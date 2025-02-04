"""
Basic Appshell with header and  navbar that collapses on mobile.  Also includes a theme switch.
"""

import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import Dash, _dash_renderer, Input, Output, State, callback, clientside_callback
_dash_renderer._set_react_version("18.2.0")



# Initialize Dash app
app = Dash(external_stylesheets=dmc.styles.ALL)

# App Logo
logo = "https://github.com/user-attachments/assets/c1ff143b-4365-4fd1-880f-3e97aab5c302"

# Theme Configuration
theme = {
    "primaryColor": "gray",
    "defaultRadius": "md",
    "components": {
        "Card": {
            "defaultProps": {"shadow": "md"}
        }
    }
}

# Theme Toggle Switch
theme_toggle = dmc.Switch(
    offLabel=DashIconify(icon="radix-icons:sun", width=15, color=dmc.DEFAULT_THEME["colors"]["yellow"][8]),
    onLabel=DashIconify(icon="radix-icons:moon", width=15, color=dmc.DEFAULT_THEME["colors"]["yellow"][6]),
    id="color-scheme-toggle",
    persistence=True,
    color="grey",
)

#   Navbar - Moved to AppShellHeader
navbar = dmc.AppShellHeader(
    dmc.Group(
        [
            dmc.Group(
                [
                    dmc.Burger(id="burger", size="sm", hiddenFrom="sm", opened=False),
                    dmc.Image(src=logo, h=40),
                    dmc.Title("Demo App", c="green"),
                ]
            ),
            theme_toggle,  # Theme toggle switch stays on the right
        ],
        justify="space-between",
        style={"flex": 1},
        h="100%",
        px="md",
    ),
    style={
        "position": "fixed",
        "top": 0,
        "left": 0,
        "width": "100%",
        "zIndex": 1000,
        "backgroundColor": "white"
    }
)

#  Sidebar
sidebar = dmc.AppShellNavbar(
    id="navbar",
    children=[
        dmc.Text("Sidebar", size="sm"),
        *[dmc.Skeleton(height=28, mt="sm", animate=False) for _ in range(15)],
    ],
    p="md",
)

# Main Content Area
content = dmc.AppShellMain("Main content goes here.")

# Updated App Layout
layout = dmc.AppShell(
    [navbar, sidebar, content],
    header={"height": 60},
    padding="md",
    navbar={
        "width": 300,
        "breakpoint": "sm",
        "collapsed": {"mobile": True},
    },
    id="appshell",
)

# Wrap with MantineProvider
app.layout = dmc.MantineProvider(layout, theme=theme)

# Fix Navbar Toggle
@app.callback(
    Output("appshell", "navbar"),
    Input("burger", "opened"),
    State("appshell", "navbar"),
)
def navbar_is_open(opened, navbar):
    navbar["collapsed"] = {"mobile": not opened}
    return navbar

clientside_callback(
    """ 
    (switchOn) => {
       document.documentElement.setAttribute('data-mantine-color-scheme', switchOn ? 'dark' : 'light');  
       return window.dash_clientside.no_update
    }
    """,
    Output("color-scheme-toggle", "id"),
    Input("color-scheme-toggle", "checked"),
)


if __name__ == "__main__":
    app.run(debug=True, port=1919)