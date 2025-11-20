import unittest
from http import HTTPStatus
from unittest.mock import Mock

from cirro_api_client.v1.models import User


def _generate_mock_client(response_data: dict):
    mock_client = Mock()
    httpx_client = Mock()
    mock_client.get_httpx_client.return_value = httpx_client
    mock_request = Mock()
    httpx_client.request.return_value = mock_request
    status_code = HTTPStatus(200)
    mock_request.status_code = status_code
    mock_request.json.return_value = response_data
    return mock_client


class TestClient(unittest.TestCase):
    def test_client_set_up(self):
        from cirro_api_client import CirroApiClient, TokenAuth
        client = CirroApiClient(auth_method=TokenAuth(token=""), base_url="https://api.cirro.bio")
        self.assertIsNotNone(client)

    def test_import_models(self):
        from cirro_api_client.v1.models import InviteUserRequest
        req = InviteUserRequest(name="Test User", organization="test", email="test")
        self.assertEqual(req.name, "Test User")
        self.assertIn('name', req.to_dict())
        self.assertEqual(len(req.additional_properties.keys()), 0)

    def test_import_api_methods(self):
        from cirro_api_client.v1.api.users import list_users
        mock_client = _generate_mock_client({'data': [Mock()], 'nextToken': None})

        response = list_users.sync(client=mock_client, limit=1)
        self.assertIsNotNone(response)
        self.assertEqual(len(response.data), 1)
        self.assertIsInstance(response.data[0], User)
