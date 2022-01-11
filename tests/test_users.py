from app import schemas
from .database import client,session


def test_root(client):
    res = client.get("/")
    assert res.status_code == 200


def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "test@gmail.com", "password": "test123"}
    )
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "test@gmail.com"
    assert res.status_code == 201


def test_login_user(client):
    res = client.post(
        "/login", data={"username": "test@gmail.com", "password": "test123"}
    )

    assert res.status_code == 200