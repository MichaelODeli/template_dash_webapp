import dash_bootstrap_components as dbc


def UnauthNavbarItems():
    """
    Функция UnauthNavbarItems возвращает компонент навигационной панели для неавторизованных пользователей.

    :return: компонент навигационной панели с ссылкой "Войти"
    """
    return [dbc.NavLink("Войти", href="/login")]


def SuccessAuthNavbarItems(username):
    """
    Функция SuccessAuthNavbarItems возвращает список компонентов навигационной панели для авторизованных пользователей.

    :param username: имя пользователя
    :return: список компонентов навигационной панели, включая ссылку на личный кабинет и кнопку выхода
    """
    return [
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Личный кабинет", href="/account?l=n"),
                dbc.DropdownMenuItem("Выйти", href="/logout"),
            ],
            nav=True,
            in_navbar=True,
            label=f"Привет, {username}!",
        )
    ]


def DisabledAuthNavbarItems():
    """
    Функция DisabledAuthNavbarItems возвращает список компонентов навигационной панели для неавторизованных пользователей.

    :return: список компонентов навигационной панели, включающий ссылку на главную страницу
    """
    return [dbc.NavLink("Главная страница", href="/")]