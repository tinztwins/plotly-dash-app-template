"""
This file contains the dropdown menu of the dashboard.
"""

from dash import dcc


def render_dropdown(dropdown_id: str, items=[''], clearable_option=False):
    """This function can be used to render a dropdown menu.

    Args:
        dropdown_id (str): Id of the dropdown menu
        items (list, optional): List of items. Defaults to [''].
        clearable_option (bool, optional): Option to clear dropdown menu. Defaults to False.

    Returns:
        dropdown (dcc.Dropdown): Dropdown html component
    """

    dropdown = dcc.Dropdown(
        id=dropdown_id,
        clearable=clearable_option,
        options=[{'label': i, 'value': i} for i in items],
        value=items[0],
    )
    return dropdown
