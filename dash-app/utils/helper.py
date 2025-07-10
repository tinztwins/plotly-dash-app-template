"""
This file contains helper function for the screens.
"""

from dash import html


def on_page_load():
    """
    Add this function to Dash Layout to trigger callbacks on page load.
    :return: Div element -> html.Div(id='trigger_on_page_load', style={'display': 'none'})
    """

    return html.Div(id='trigger_on_page_load', style={'display': 'none'})
