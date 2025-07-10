"""
This file contains the navigation bar of the app.
"""

import dash_bootstrap_components as dbc

from environment.settings import VERSION

# import own style (see /assets)
from assets.style import MAIN_COLORS

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Dashboard", href="/dashboard")),
    ],
    brand="Gapminder " + VERSION,
    brand_href="/",
    color=MAIN_COLORS["primary"],
    sticky='top',
    links_left=True,
    dark=True
)
