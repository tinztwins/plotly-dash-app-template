"""
This file contains the map plot.
"""

from dash import dcc
import plotly.express as px


def bubble_map(df, variable):
    dict_variable = {'Population':'pop', 'Life expectancy':'lifeExp', 'GDP per capita':'gdpPercap'}
    variable = dict_variable[variable]

    fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
                     hover_name="country", size=variable,
                     animation_frame="year",
                     projection="natural earth")
    
    return dcc.Graph(figure=fig)
