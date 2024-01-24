import unittest

from cirro_api_client import Configuration, CirroApiClient


class TestClient(unittest.TestCase):
    def test_client_set_up(self):
        configuration = Configuration()
        client = CirroApiClient(configuration=configuration)
        self.assertIsNotNone(client)
