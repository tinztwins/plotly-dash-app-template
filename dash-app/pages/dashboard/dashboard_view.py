"""
This file contains the dashboard screen.
"""

import dash_bootstrap_components as dbc
from dash import html

# import components
from components.dropdown import render_dropdown
from components.navbar import navbar


def render_dashboard():
    """
    :return: html.Div with dashboard content
    """
    return html.Div([
        navbar,
        html.Div(
            [
                html.Br(),
                dbc.Container(
                    fluid=True,
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    width=2,
                                    children=dbc.Card(
                                        [
                                            dbc.CardHeader("Variables"),
                                            dbc.CardBody(
                                                [
                                                    render_dropdown(dropdown_id="dropdown-choose-item", items=['Population', 'Life expectancy', 'GDP per capita'])
                                                ]
                                            )
                                        ],
                                        style={'height': "84vh"},
                                    )
                                ),
                                dbc.Col(
                                    width=10,
                                    children=dbc.Card(
                                        [
                                            dbc.CardHeader("World map"),
                                            dbc.CardBody(
                                                [
                                                    html.Div(id='div-vis')
                                                ]
                                            )
                                        ],
                                        style={'height': '84vh'}
                                    )
                                )
                            ]
                        )
                    ]
                ),
            ]
        )
    ])
