import pytest
from fastapi.testclient import TestClient
from order_service import app

@pytest.fixture
def test_client():
    return TestClient(app)

def test_create_order_integration(test_client):
    response = test_client.post(
        "/create-order/",
        json={"product": "Pen", "quantity": 3, "price": 5.00},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "Order placed successfully"