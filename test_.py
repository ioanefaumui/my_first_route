from flask import Flask
from flask.testing import FlaskClient
from pytest import fixture, fail
from datetime import datetime


@fixture
def app():
    try:
        return __import__("flask_routes").app
    except ModuleNotFoundError:
        fail("Verifique se o nome do arquivo é `flask_routes`")
    except AttributeError:
        fail("Verifique se a instancia de Flask eh `app`")


@fixture
def route_matcher(app: Flask):
    return app.url_map.bind("").match


@fixture
def client(app: Flask):
    with app.test_client() as client:
        yield client


def test_verify_if_route_detetime_was_defined(route_matcher):
    assert route_matcher(
        "/current_datetime"
    ), "Verifique se voce definiu a rota '/datetime'"


def test_verify_if_route_home_was_defined(route_matcher):
    assert route_matcher("/"), "Verifique se voce definiu a rota '/'"


def test_verify_is_getting_from_home_route(client: FlaskClient):
    response = client.get("/")
    expected = {"data": "Hello Flask"}

    assert response.status_code == 200
    assert response.json == expected
    assert type(response.json) == dict


def test_verify_is_getting_from_datetime_route(client: FlaskClient):
    response = client.get("/current_datetime")
    curr_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")
    curr_hour = datetime.now().hour
    msg = "Boa noite!"
    if curr_hour < 12:
        msg = "Bom dia!"

    elif curr_hour < 18:
        msg = "Boa tarde!"

    expected = {"current_datetime": curr_datetime, "message": msg}

    assert response.status_code == 200
    assert response.json == expected
    assert type(response.json) == dict
