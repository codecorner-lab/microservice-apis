import pytest
from order_service import app, Order

@pytest.fixture
def test_client():
    from fastapi.testclient import TestClient
    return TestClient(app)

def test_create_order_success(test_client, mocker):
    mocker.patch("order_service.requests.post", return_value=mocker.Mock(status_code=200))

    response = test_client.post(
        "/create-order/",
        json={"product": "Book", "quantity": 2, "price": 15.00},
    )
    assert response.status_code == 200
    assert response.json() == {
        "status": "Order placed successfully",
        "order": {"product": "Book", "quantity":2, "price": 15.0},
    }

def test_create_order_payment_failure(test_client, mocker):
    mocker.patch("order_service.requests.post", return_value=mocker.Mock(status_code=500))

    response = test_client.post(
        "/create-order/",
        json={"product": "Book", "quantity": 1, "price": 20.00},
    )

    assert response.status_code == 200
    assert response.json()["status"] == "Payment failed, could not reach payment service"