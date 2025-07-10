"""
This file contains the 'Page not found' page.
"""

from dash import html


def page_not_found():
    """Page not found

    Returns:
        html.Div: Div element
    """

    return html.Div([
        html.H1('404'),
        html.H2('Page not found'),
        html.H2('Oh, something went wrong!')
    ])
