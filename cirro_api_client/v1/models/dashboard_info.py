from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DashboardInfo")


@_attrs_define
class DashboardInfo:
    """ """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        dashboard_info = cls()

        dashboard_info.additional_properties = d
        return dashboard_info

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
