"""
This file is the entry point of the app.
Run this app with `python index.py` and
visit http://127.0.0.1:7000/ in your web browser.
"""

from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# import pages
from pages.dashboard.dashboard_view import render_dashboard
from pages.dashboard.dashboard_controller import *
from pages.page_not_found import page_not_found

from app import app

from environment.settings import APP_HOST, APP_PORT, APP_DEBUG

server = app.server

def serve_content():
    """
    :return: html div component
    """
    return html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])


app.layout = serve_content()


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    """
    :param pathname: path of the actual page
    :return: page
    """
    print('show page')

    if pathname in '/' or pathname in '/dashboard':
        return render_dashboard()
    return page_not_found()


if __name__ == '__main__':
    app.run_server(debug=APP_DEBUG, host=APP_HOST, port=APP_PORT)
