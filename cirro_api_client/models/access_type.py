# coding: utf-8

"""
    Cirro Data

    Cirro Data Platform service API

    The version of the OpenAPI document: latest
    Contact: support@cirro.bio
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class AccessType(str, Enum):
    """
    AccessType
    """

    """
    allowed enum values
    """
    DATASET_UPLOAD = 'DATASET_UPLOAD'
    SAMPLESHEET_UPLOAD = 'SAMPLESHEET_UPLOAD'
    REFERENCE_UPLOAD = 'REFERENCE_UPLOAD'
    PROJECT_DOWNLOAD = 'PROJECT_DOWNLOAD'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AccessType from a JSON string"""
        return cls(json.loads(json_str))


