import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import Dash, _dash_renderer, Input, Output,dcc, State, callback, clientside_callback
_dash_renderer._set_react_version("18.2.0")

# Import page layouts
from menu1 import layout as menu1_layout
from menu2 import layout as menu2_layout
from menu3 import layout as menu3_layout

# Initialize Dash app
app = Dash(__name__, suppress_callback_exceptions=True)

# App logo
logo = "https://github.com/user-attachments/assets/c1ff143b-4365-4fd1-880f-3e97aab5c302"

# Theme toggle switch
theme_toggle = dmc.Switch(
    offLabel=DashIconify(icon="radix-icons:sun", width=15, color=dmc.DEFAULT_THEME["colors"]["yellow"][8]),
    onLabel=DashIconify(icon="radix-icons:moon", width=15, color=dmc.DEFAULT_THEME["colors"]["yellow"][6]),
    id="color-scheme-toggle",
    persistence=True,
    color="grey",
)

def get_icon(icon):
    return DashIconify(icon=icon, height=16)

# # Navbar with Menu Links
# navbar = dmc.AppShellHeader(
#     dmc.Group(
#         [
#             dmc.Image(src=logo, h=40),  # Logo
#             dmc.Title("Demo App", c="green"),  # Title
#             dmc.NavLink(label="Menu 1", href="/menu1", className="nav-link", leftSection=get_icon(icon="bi:house-door-fill"),),
#             dmc.NavLink(label="Menu 2", href="/menu2", className="nav-link"),
#             dmc.NavLink(label="Menu 3", href="/menu3", className="nav-link"),

#             # dmc.Group(
#             #     [
#             #         dmc.NavLink(label="Menu 1", href="/menu1", className="nav-link", leftSection=get_icon(icon="bi:house-door-fill"),),
#             #         dmc.NavLink(label="Menu 2", href="/menu2", className="nav-link"),
#             #         dmc.NavLink(label="Menu 3", href="/menu3", className="nav-link"),
#             #     ],
#             #     gap="md"
#             # ),
#             theme_toggle,  # Theme Toggle
#         ],
#         justify="space-between",
#         style={"flex": 1},
#         h="100%",
#         px="md",
#     ),
#     style={
#         "position": "fixed",
#         "top": 0,
#         "left": 0,
#         "width": "100%",
#         "zIndex": 1000,
#         "backgroundColor": "white"
#     }
# )
# Navbar with Menu Links
navbar = dmc.AppShellHeader(
    dmc.Group(
        [
            # Left side: Logo and title
            dmc.Group(
                [
                    dmc.Image(src=logo, h=40),
                    dmc.Title("Demo App", c="green"),
                ],
                gap="md",
                style={"flex": 1},  
            ),

          
            dmc.Group(
                [
                    dmc.Anchor("Menu 1", href="/menu1", className="nav-link"  , underline=False),
                    dmc.Anchor("Menu 2", href="/menu2", className="nav-link", underline=False),
                    dmc.Anchor("Menu 3", href="/menu3", className="nav-link", underline=False),
                ],
                gap="lg",  
                align="center",
                style={"flex": 1, "justifyContent": "center"},  # Centers the menu links
            ),

            # Right side: Theme toggle
            theme_toggle,
        ],
        justify="space-between",
        align="center",
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
        "backgroundColor": "white",
        "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.1)" 
    }
)


# Layout with dynamic page content
app.layout = dmc.MantineProvider(
    dmc.AppShell(
        [navbar, dmc.AppShellMain(id="page-content", style={"marginTop": "60px"}, children=[])],
        # header={"height": 60},
        padding="md",
        id="appshell",
    )
)

# Page navigation callback
@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/menu1":
        return menu1_layout
    elif pathname == "/menu2":
        return menu2_layout
    elif pathname == "/menu3":
        return menu3_layout
    else:
        return dmc.Text("Welcome! Select a menu from the navbar.")

#  Dark Mode Toggle
app.clientside_callback(
    """ 
    (switchOn) => {
       document.documentElement.setAttribute('data-mantine-color-scheme', switchOn ? 'dark' : 'light');  
       return dash_clientside.no_update
    }
    """,
    Output("color-scheme-toggle", "id"),
    Input("color-scheme-toggle", "checked"),
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True , port=3939)
