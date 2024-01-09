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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from cirro_api_client.models.custom_pipeline_settings import CustomPipelineSettings
from cirro_api_client.models.executor import Executor
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProcessDetail(BaseModel):
    """
    ProcessDetail
    """ # noqa: E501
    id: StrictStr = Field(description="Unique ID of the Process")
    name: StrictStr
    description: StrictStr
    executor: Executor
    documentation_url: StrictStr = Field(alias="documentationUrl")
    file_requirements_message: Optional[StrictStr] = Field(default=None, description="Description of the files to be uploaded (optional)", alias="fileRequirementsMessage")
    child_process_ids: List[StrictStr] = Field(alias="childProcessIds")
    parent_process_ids: List[StrictStr] = Field(alias="parentProcessIds")
    owner: StrictStr
    linked_project_ids: List[StrictStr] = Field(alias="linkedProjectIds")
    custom_settings: CustomPipelineSettings = Field(alias="customSettings")
    is_archived: StrictBool = Field(alias="isArchived")
    __properties: ClassVar[List[str]] = ["id", "name", "description", "executor", "documentationUrl", "fileRequirementsMessage", "childProcessIds", "parentProcessIds", "owner", "linkedProjectIds", "customSettings", "isArchived"]

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
        """Create an instance of ProcessDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of custom_settings
        if self.custom_settings:
            _dict['customSettings'] = self.custom_settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProcessDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "executor": obj.get("executor"),
            "documentationUrl": obj.get("documentationUrl"),
            "fileRequirementsMessage": obj.get("fileRequirementsMessage"),
            "childProcessIds": obj.get("childProcessIds"),
            "parentProcessIds": obj.get("parentProcessIds"),
            "owner": obj.get("owner"),
            "linkedProjectIds": obj.get("linkedProjectIds"),
            "customSettings": CustomPipelineSettings.from_dict(obj.get("customSettings")) if obj.get("customSettings") is not None else None,
            "isArchived": obj.get("isArchived")
        })
        return _obj


