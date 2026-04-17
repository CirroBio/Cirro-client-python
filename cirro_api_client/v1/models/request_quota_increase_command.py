from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RequestQuotaIncreaseCommand")


@_attrs_define
class RequestQuotaIncreaseCommand:
    """
    Attributes:
        service_code (str):
        quota_code (str):
        value (float):
    """

    service_code: str
    quota_code: str
    value: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_code = self.service_code

        quota_code = self.quota_code

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceCode": service_code,
                "quotaCode": quota_code,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_code = d.pop("serviceCode")

        quota_code = d.pop("quotaCode")

        value = d.pop("value")

        request_quota_increase_command = cls(
            service_code=service_code,
            quota_code=quota_code,
            value=value,
        )

        request_quota_increase_command.additional_properties = d
        return request_quota_increase_command

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
