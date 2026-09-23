from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_info import AuthInfo
    from ..models.tenant_info import TenantInfo
    from ..models.version_info import VersionInfo


T = TypeVar("T", bound="SystemInfoResponse")


@_attrs_define
class SystemInfoResponse:
    """
    Attributes:
        resources_bucket (str):
        references_bucket (str):
        live_endpoint (str):
        agent_endpoint (str):
        region (str):
        system_message (str):
        maintenance_mode_enabled (bool):
        tenant_info (TenantInfo):
        auth (AuthInfo):
        backend_version (None | Unset | VersionInfo):
        resources_version (None | Unset | VersionInfo):
        project_resource_version (None | Unset | VersionInfo):
    """

    resources_bucket: str
    references_bucket: str
    live_endpoint: str
    agent_endpoint: str
    region: str
    system_message: str
    maintenance_mode_enabled: bool
    tenant_info: TenantInfo
    auth: AuthInfo
    backend_version: None | Unset | VersionInfo = UNSET
    resources_version: None | Unset | VersionInfo = UNSET
    project_resource_version: None | Unset | VersionInfo = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.version_info import VersionInfo

        resources_bucket = self.resources_bucket

        references_bucket = self.references_bucket

        live_endpoint = self.live_endpoint

        agent_endpoint = self.agent_endpoint

        region = self.region

        system_message = self.system_message

        maintenance_mode_enabled = self.maintenance_mode_enabled

        tenant_info = self.tenant_info.to_dict()

        auth = self.auth.to_dict()

        backend_version: dict[str, Any] | None | Unset
        if isinstance(self.backend_version, Unset):
            backend_version = UNSET
        elif isinstance(self.backend_version, VersionInfo):
            backend_version = self.backend_version.to_dict()
        else:
            backend_version = self.backend_version

        resources_version: dict[str, Any] | None | Unset
        if isinstance(self.resources_version, Unset):
            resources_version = UNSET
        elif isinstance(self.resources_version, VersionInfo):
            resources_version = self.resources_version.to_dict()
        else:
            resources_version = self.resources_version

        project_resource_version: dict[str, Any] | None | Unset
        if isinstance(self.project_resource_version, Unset):
            project_resource_version = UNSET
        elif isinstance(self.project_resource_version, VersionInfo):
            project_resource_version = self.project_resource_version.to_dict()
        else:
            project_resource_version = self.project_resource_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourcesBucket": resources_bucket,
                "referencesBucket": references_bucket,
                "liveEndpoint": live_endpoint,
                "agentEndpoint": agent_endpoint,
                "region": region,
                "systemMessage": system_message,
                "maintenanceModeEnabled": maintenance_mode_enabled,
                "tenantInfo": tenant_info,
                "auth": auth,
            }
        )
        if backend_version is not UNSET:
            field_dict["backendVersion"] = backend_version
        if resources_version is not UNSET:
            field_dict["resourcesVersion"] = resources_version
        if project_resource_version is not UNSET:
            field_dict["projectResourceVersion"] = project_resource_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_info import AuthInfo
        from ..models.tenant_info import TenantInfo
        from ..models.version_info import VersionInfo

        d = dict(src_dict)
        resources_bucket = d.pop("resourcesBucket")

        references_bucket = d.pop("referencesBucket")

        live_endpoint = d.pop("liveEndpoint")

        agent_endpoint = d.pop("agentEndpoint")

        region = d.pop("region")

        system_message = d.pop("systemMessage")

        maintenance_mode_enabled = d.pop("maintenanceModeEnabled")

        tenant_info = TenantInfo.from_dict(d.pop("tenantInfo"))

        auth = AuthInfo.from_dict(d.pop("auth"))

        def _parse_backend_version(data: object) -> None | Unset | VersionInfo:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                backend_version_type_1 = VersionInfo.from_dict(data)

                return backend_version_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VersionInfo, data)

        backend_version = _parse_backend_version(d.pop("backendVersion", UNSET))

        def _parse_resources_version(data: object) -> None | Unset | VersionInfo:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resources_version_type_1 = VersionInfo.from_dict(data)

                return resources_version_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VersionInfo, data)

        resources_version = _parse_resources_version(d.pop("resourcesVersion", UNSET))

        def _parse_project_resource_version(data: object) -> None | Unset | VersionInfo:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                project_resource_version_type_1 = VersionInfo.from_dict(data)

                return project_resource_version_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VersionInfo, data)

        project_resource_version = _parse_project_resource_version(d.pop("projectResourceVersion", UNSET))

        system_info_response = cls(
            resources_bucket=resources_bucket,
            references_bucket=references_bucket,
            live_endpoint=live_endpoint,
            agent_endpoint=agent_endpoint,
            region=region,
            system_message=system_message,
            maintenance_mode_enabled=maintenance_mode_enabled,
            tenant_info=tenant_info,
            auth=auth,
            backend_version=backend_version,
            resources_version=resources_version,
            project_resource_version=project_resource_version,
        )

        system_info_response.additional_properties = d
        return system_info_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
