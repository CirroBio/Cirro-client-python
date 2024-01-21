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

from cirro_api_client.models.file_access_request import FileAccessRequest

class TestFileAccessRequest(unittest.TestCase):
    """FileAccessRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileAccessRequest:
        """Test FileAccessRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileAccessRequest`
        """
        model = FileAccessRequest()
        if include_optional:
            return FileAccessRequest(
                access_type = 'DATASET_UPLOAD',
                dataset_id = '',
                token_lifetime_hours = 56
            )
        else:
            return FileAccessRequest(
                access_type = 'DATASET_UPLOAD',
        )
        """

    def testFileAccessRequest(self):
        """Test FileAccessRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
