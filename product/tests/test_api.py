import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_list_api_product():
    client = APIClient()
    response = client.get(path='/product/list/2', format='json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_api_category():
    client = APIClient()
    data = {'name': 'تبلت'}
    response = client.post(path='/product/category/create/', data=data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_put_api_product():
    client = APIClient()
    data = {'name': 'تبلت'}
    response = client.put(path='/product/1', data=data)
    assert response.status_code == 301