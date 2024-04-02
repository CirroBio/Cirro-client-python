from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resources_info import ResourcesInfo
    from ..models.tenant_info import TenantInfo


T = TypeVar("T", bound="SystemInfoResponse")


@_attrs_define
class SystemInfoResponse:
    """
    Attributes:
        sdk_app_id (str):
        resources_bucket (str):
        references_bucket (str):
        region (str):
        system_message (str):
        commit_hash (str):
        version (str):
        resources_info (ResourcesInfo):
        tenant_info (TenantInfo):
    """

    sdk_app_id: str
    resources_bucket: str
    references_bucket: str
    region: str
    system_message: str
    commit_hash: str
    version: str
    resources_info: "ResourcesInfo"
    tenant_info: "TenantInfo"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sdk_app_id = self.sdk_app_id

        resources_bucket = self.resources_bucket

        references_bucket = self.references_bucket

        region = self.region

        system_message = self.system_message

        commit_hash = self.commit_hash

        version = self.version

        resources_info = self.resources_info.to_dict()

        tenant_info = self.tenant_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sdkAppId": sdk_app_id,
                "resourcesBucket": resources_bucket,
                "referencesBucket": references_bucket,
                "region": region,
                "systemMessage": system_message,
                "commitHash": commit_hash,
                "version": version,
                "resourcesInfo": resources_info,
                "tenantInfo": tenant_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.resources_info import ResourcesInfo
        from ..models.tenant_info import TenantInfo

        d = src_dict.copy()
        sdk_app_id = d.pop("sdkAppId")

        resources_bucket = d.pop("resourcesBucket")

        references_bucket = d.pop("referencesBucket")

        region = d.pop("region")

        system_message = d.pop("systemMessage")

        commit_hash = d.pop("commitHash")

        version = d.pop("version")

        resources_info = ResourcesInfo.from_dict(d.pop("resourcesInfo"))

        tenant_info = TenantInfo.from_dict(d.pop("tenantInfo"))

        system_info_response = cls(
            sdk_app_id=sdk_app_id,
            resources_bucket=resources_bucket,
            references_bucket=references_bucket,
            region=region,
            system_message=system_message,
            commit_hash=commit_hash,
            version=version,
            resources_info=resources_info,
            tenant_info=tenant_info,
        )

        system_info_response.additional_properties = d
        return system_info_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())
