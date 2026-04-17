from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudQuota")


@_attrs_define
class CloudQuota:
    """
    Attributes:
        name (str):
        description (str):
        service (str):
        code (str):
        applied_quota (float):
        has_open_request (bool):
        requested_quota (float | None | Unset):
    """

    name: str
    description: str
    service: str
    code: str
    applied_quota: float
    has_open_request: bool
    requested_quota: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        service = self.service

        code = self.code

        applied_quota = self.applied_quota

        has_open_request = self.has_open_request

        requested_quota: float | None | Unset
        if isinstance(self.requested_quota, Unset):
            requested_quota = UNSET
        else:
            requested_quota = self.requested_quota

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "service": service,
                "code": code,
                "appliedQuota": applied_quota,
                "hasOpenRequest": has_open_request,
            }
        )
        if requested_quota is not UNSET:
            field_dict["requestedQuota"] = requested_quota

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        service = d.pop("service")

        code = d.pop("code")

        applied_quota = d.pop("appliedQuota")

        has_open_request = d.pop("hasOpenRequest")

        def _parse_requested_quota(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        requested_quota = _parse_requested_quota(d.pop("requestedQuota", UNSET))

        cloud_quota = cls(
            name=name,
            description=description,
            service=service,
            code=code,
            applied_quota=applied_quota,
            has_open_request=has_open_request,
            requested_quota=requested_quota,
        )

        cloud_quota.additional_properties = d
        return cloud_quota

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
