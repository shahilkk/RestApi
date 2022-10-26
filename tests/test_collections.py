from rest_framework.test import APIClient
from rest_framework import status
import pytest


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_annoymous_returns_401(self):
        # AAA(arrage,Act,Asserts)
        client=APIClient()
        response = client.post('/store/collections/',{'title':'shahil test'})
        assert response.status_code ==  status.HTTP_401_UNAUTHORIZED

            
            
        