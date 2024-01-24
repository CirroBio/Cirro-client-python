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
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from cirro_api_client.models.budget_period import BudgetPeriod
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProjectSettings(BaseModel):
    """
    ProjectSettings
    """ # noqa: E501
    budget_amount: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Total allowed cost for the budget period", alias="budgetAmount")
    budget_period: BudgetPeriod = Field(alias="budgetPeriod")
    dragen_ami: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="AMI ID for the DRAGEN compute environment (if enabled)", alias="dragenAmi")
    enable_compute: Optional[StrictBool] = Field(default=True, description="Enables the default compute environment", alias="enableCompute")
    enable_dragen: Optional[StrictBool] = Field(default=False, description="Enables the DRAGEN compute environment", alias="enableDragen")
    enable_backup: Optional[StrictBool] = Field(default=False, description="Enables the AWS Backup service for S3", alias="enableBackup")
    enable_sftp: Optional[StrictBool] = Field(default=False, description="Enables access to files over SFTP", alias="enableSftp")
    max_f1_vcpu: Optional[Annotated[int, Field(le=1000, strict=True, ge=0)]] = Field(default=0, description="Service quota limit for On Demand F1 instances", alias="maxF1VCPU")
    max_spot_vcpu: Optional[Annotated[int, Field(le=10000, strict=True, ge=0)]] = Field(default=0, description="Service quota limit for SPOT instances", alias="maxSpotVCPU")
    retention_policy_days: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=7, description="Days to keep deleted datasets before being permanently erased", alias="retentionPolicyDays")
    service_connections: List[StrictStr] = Field(alias="serviceConnections")
    create_vpc: Optional[StrictBool] = Field(default=False, description="Creates a default VPC for the compute environment, if false, VPC ID must be provided", alias="createVpc")
    vpc_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="VPC that the compute environment will use", alias="vpcId")
    batch_subnets: Optional[List[StrictStr]] = Field(default=None, description="List of subnets that the compute environment will use", alias="batchSubnets")
    kms_arn: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="KMS Key ARN to encrypt S3 objects, one will be created if the arn is not provided", alias="kmsArn")
    __properties: ClassVar[List[str]] = ["budgetAmount", "budgetPeriod", "dragenAmi", "enableCompute", "enableDragen", "enableBackup", "enableSftp", "maxF1VCPU", "maxSpotVCPU", "retentionPolicyDays", "serviceConnections", "createVpc", "vpcId", "batchSubnets", "kmsArn"]

    @field_validator('dragen_ami')
    def dragen_ami_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^ami-*$", value):
            raise ValueError(r"must validate the regular expression /^ami-*$/")
        return value

    @field_validator('vpc_id')
    def vpc_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^vpc-*$", value):
            raise ValueError(r"must validate the regular expression /^vpc-*$/")
        return value

    @field_validator('kms_arn')
    def kms_arn_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^arn:aws:*$", value):
            raise ValueError(r"must validate the regular expression /^arn:aws:*$/")
        return value

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
        """Create an instance of ProjectSettings from a JSON string"""
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
        # set to None if dragen_ami (nullable) is None
        # and model_fields_set contains the field
        if self.dragen_ami is None and "dragen_ami" in self.model_fields_set:
            _dict['dragenAmi'] = None

        # set to None if vpc_id (nullable) is None
        # and model_fields_set contains the field
        if self.vpc_id is None and "vpc_id" in self.model_fields_set:
            _dict['vpcId'] = None

        # set to None if batch_subnets (nullable) is None
        # and model_fields_set contains the field
        if self.batch_subnets is None and "batch_subnets" in self.model_fields_set:
            _dict['batchSubnets'] = None

        # set to None if kms_arn (nullable) is None
        # and model_fields_set contains the field
        if self.kms_arn is None and "kms_arn" in self.model_fields_set:
            _dict['kmsArn'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProjectSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "budgetAmount": obj.get("budgetAmount"),
            "budgetPeriod": obj.get("budgetPeriod"),
            "dragenAmi": obj.get("dragenAmi"),
            "enableCompute": obj.get("enableCompute") if obj.get("enableCompute") is not None else True,
            "enableDragen": obj.get("enableDragen") if obj.get("enableDragen") is not None else False,
            "enableBackup": obj.get("enableBackup") if obj.get("enableBackup") is not None else False,
            "enableSftp": obj.get("enableSftp") if obj.get("enableSftp") is not None else False,
            "maxF1VCPU": obj.get("maxF1VCPU") if obj.get("maxF1VCPU") is not None else 0,
            "maxSpotVCPU": obj.get("maxSpotVCPU") if obj.get("maxSpotVCPU") is not None else 0,
            "retentionPolicyDays": obj.get("retentionPolicyDays") if obj.get("retentionPolicyDays") is not None else 7,
            "serviceConnections": obj.get("serviceConnections"),
            "createVpc": obj.get("createVpc") if obj.get("createVpc") is not None else False,
            "vpcId": obj.get("vpcId"),
            "batchSubnets": obj.get("batchSubnets"),
            "kmsArn": obj.get("kmsArn")
        })
        return _obj


