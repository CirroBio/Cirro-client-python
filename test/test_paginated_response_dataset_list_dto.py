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

from cirro_api_client.models.paginated_response_dataset_list_dto import PaginatedResponseDatasetListDto

class TestPaginatedResponseDatasetListDto(unittest.TestCase):
    """PaginatedResponseDatasetListDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedResponseDatasetListDto:
        """Test PaginatedResponseDatasetListDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedResponseDatasetListDto`
        """
        model = PaginatedResponseDatasetListDto()
        if include_optional:
            return PaginatedResponseDatasetListDto(
                data = [
                    cirro_api_client.models.dataset.Dataset(
                        id = '0', 
                        name = '', 
                        description = '', 
                        project_id = '', 
                        process_id = '', 
                        source_dataset_ids = [
                            ''
                            ], 
                        status = 'COMPLETED', 
                        tags = [
                            cirro_api_client.models.tag.Tag(
                                key = '', 
                                value = '', 
                                editable = True, )
                            ], 
                        created_by = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                next_token = ''
            )
        else:
            return PaginatedResponseDatasetListDto(
                data = [
                    cirro_api_client.models.dataset.Dataset(
                        id = '0', 
                        name = '', 
                        description = '', 
                        project_id = '', 
                        process_id = '', 
                        source_dataset_ids = [
                            ''
                            ], 
                        status = 'COMPLETED', 
                        tags = [
                            cirro_api_client.models.tag.Tag(
                                key = '', 
                                value = '', 
                                editable = True, )
                            ], 
                        created_by = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                next_token = '',
        )
        """

    def testPaginatedResponseDatasetListDto(self):
        """Test PaginatedResponseDatasetListDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
