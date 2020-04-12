from app import api
import aiohttp_cors, pathlib

static_path = str(pathlib.Path(__file__).parent / "static")


def setup_ui_routes(app):
    """

    :param app:
    :return:
    """
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })
    app.router.add_routes(api.routes)
    app.router.add_static('/static/', path=static_path, name='static')
    for route in list(app.router.routes()):
        cors.add(route)
