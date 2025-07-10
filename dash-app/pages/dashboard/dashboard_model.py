import plotly.express as px


def get_map_data():
     df = px.data.gapminder()
     return df


def map_dataframe():
    return get_map_data()