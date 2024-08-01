from dash import html, register_page

register_page(
    __name__,
    path="/logout",
)

layout = html.Center(
    [
        html.H5("Вы успешно вышли из своего аккаунта."),
    ],
    style={"margin-top": "70px"},
)
