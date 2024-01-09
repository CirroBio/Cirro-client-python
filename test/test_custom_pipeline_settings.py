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

from cirro.api.models.custom_pipeline_settings import CustomPipelineSettings

class TestCustomPipelineSettings(unittest.TestCase):
    """CustomPipelineSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomPipelineSettings:
        """Test CustomPipelineSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomPipelineSettings`
        """
        model = CustomPipelineSettings()
        if include_optional:
            return CustomPipelineSettings(
                repository = '',
                branch = '',
                folder = '',
                last_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sync_status = '',
                commit_hash = ''
            )
        else:
            return CustomPipelineSettings(
                repository = '',
                branch = '',
                folder = '',
                last_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sync_status = '',
                commit_hash = '',
        )
        """

    def testCustomPipelineSettings(self):
        """Test CustomPipelineSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
