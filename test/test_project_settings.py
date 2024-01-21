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

from cirro_api_client.models.project_settings import ProjectSettings

class TestProjectSettings(unittest.TestCase):
    """ProjectSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectSettings:
        """Test ProjectSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectSettings`
        """
        model = ProjectSettings()
        if include_optional:
            return ProjectSettings(
                budget_amount = 0,
                budget_period = None,
                dragen_ami = 'ami----------------------',
                enable_compute = True,
                enable_dragen = True,
                enable_backup = True,
                enable_sftp = True,
                max_f1_vcpu = 0,
                max_spot_vcpu = 0,
                retention_policy_days = 0,
                service_connections = [
                    ''
                    ],
                create_vpc = True,
                vpc_id = 'vpc----------------------',
                batch_subnets = [
                    ''
                    ],
                kms_arn = 'arn:aws::::::::::::::::::::::'
            )
        else:
            return ProjectSettings(
                service_connections = [
                    ''
                    ],
        )
        """

    def testProjectSettings(self):
        """Test ProjectSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
