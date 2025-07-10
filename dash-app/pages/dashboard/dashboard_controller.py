from dash.dependencies import Input, Output

from app import app

from pages.dashboard.dashboard_model import map_dataframe

# import components
from plots.map_plot import *


@app.callback(
    Output(component_id='div-vis', component_property='children'),
    Input(component_id='dropdown-choose-item', component_property='value')
)
def update_vis(variable):
    df = map_dataframe()
    fig = bubble_map(df, variable)

    return fig