# coding: utf-8

"""
    Cirro Data

    Cirro Data Platform service API

    The version of the OpenAPI document: latest
    Contact: support@cirro.bio
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cirro_api_client.models.contact import Contact

class TestContact(unittest.TestCase):
    """Contact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Contact:
        """Test Contact
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Contact`
        """
        model = Contact()
        if include_optional:
            return Contact(
                name = '',
                organization = '',
                email = '',
                phone = ''
            )
        else:
            return Contact(
                name = '',
                organization = '',
                email = '',
                phone = '',
        )
        """

    def testContact(self):
        """Test Contact"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
