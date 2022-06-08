import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_with_authenticated_client():
   client = APIClient()
   data = {"email": "ali.pishgard@gmail.com", "password": "Test@1234"}
   response = client.post(path='/user/login/', data=data)
   print(response.data)
   assert response.status_code == 200