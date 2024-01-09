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

from cirro.api.models.dataset_assets_manifest import DatasetAssetsManifest

class TestDatasetAssetsManifest(unittest.TestCase):
    """DatasetAssetsManifest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatasetAssetsManifest:
        """Test DatasetAssetsManifest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatasetAssetsManifest`
        """
        model = DatasetAssetsManifest()
        if include_optional:
            return DatasetAssetsManifest(
                domain = 's3://project-1a1a/datasets/1a1a',
                files = [
                    cirro.api.models.dataset_file.DatasetFile(
                        path = 'data/fastq/SRX12875516_SRR16674827_1.fastq.gz', 
                        size = 1435658507, 
                        metadata = {"read":1}, )
                    ],
                viz = [
                    cirro.api.models.dataset_viz.DatasetViz(
                        name = '', 
                        desc = '', 
                        type = 'vitescce', 
                        config = '', )
                    ]
            )
        else:
            return DatasetAssetsManifest(
        )
        """

    def testDatasetAssetsManifest(self):
        """Test DatasetAssetsManifest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
