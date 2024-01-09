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
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from cirro_api_client.models.dataset_file import DatasetFile
from cirro_api_client.models.dataset_viz import DatasetViz
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DatasetAssetsManifest(BaseModel):
    """
    DatasetAssetsManifest
    """ # noqa: E501
    domain: Optional[StrictStr] = Field(default=None, description="Base URL for files")
    files: Optional[List[DatasetFile]] = Field(default=None, description="List of files in the dataset, including metadata")
    viz: Optional[List[DatasetViz]] = Field(default=None, description="List of viz to render for the dataset")
    __properties: ClassVar[List[str]] = ["domain", "files", "viz"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DatasetAssetsManifest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item in self.files:
                if _item:
                    _items.append(_item.to_dict())
            _dict['files'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in viz (list)
        _items = []
        if self.viz:
            for _item in self.viz:
                if _item:
                    _items.append(_item.to_dict())
            _dict['viz'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DatasetAssetsManifest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "domain": obj.get("domain"),
            "files": [DatasetFile.from_dict(_item) for _item in obj.get("files")] if obj.get("files") is not None else None,
            "viz": [DatasetViz.from_dict(_item) for _item in obj.get("viz")] if obj.get("viz") is not None else None
        })
        return _obj


