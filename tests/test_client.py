import unittest

from cirro_api_client import CirroApiClient, TokenAuth


class TestClient(unittest.TestCase):
    def test_client_set_up(self):
        client = CirroApiClient(auth_method=TokenAuth(token=""), base_url="https://api.cirro.bio")
        self.assertIsNotNone(client)
