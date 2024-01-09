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

from cirro.api.models.system_info_response import SystemInfoResponse

class TestSystemInfoResponse(unittest.TestCase):
    """SystemInfoResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemInfoResponse:
        """Test SystemInfoResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemInfoResponse`
        """
        model = SystemInfoResponse()
        if include_optional:
            return SystemInfoResponse(
                sdk_app_id = '',
                resources_bucket = '',
                data_endpoint = '',
                region = '',
                system_message = '',
                commit_hash = '',
                version = ''
            )
        else:
            return SystemInfoResponse(
                sdk_app_id = '',
                resources_bucket = '',
                data_endpoint = '',
                region = '',
                system_message = '',
                commit_hash = '',
                version = '',
        )
        """

    def testSystemInfoResponse(self):
        """Test SystemInfoResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
