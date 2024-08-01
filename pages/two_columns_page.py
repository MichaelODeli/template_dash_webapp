from dash import html, register_page
import dash_bootstrap_components as dbc
from flask_login import current_user
from controllers import users_controllers

register_page(
    __name__,
    path="/temp_1",
)


def layout(**kwargs):
    if not current_user.is_authenticated:
        return html.Div()
    else:
        username = current_user.get_id()
        userdata = users_controllers.get_user_info(username=username)

        return dbc.Row(
            [
                dbc.Col(className="adaptive-hide adaptive-width", width=3),
                dbc.Col(["Колонка 1"], md=3, xs=6, class_name="adaptive-width"),
                dbc.Col(["Колонка 2"], md=3, xs=6, class_name="adaptive-width"),
                dbc.Col(className="adaptive-hide", width=3),
            ],
            style={"paddingTop": "33dvh"},
            class_name="adaptive-block",
        )
