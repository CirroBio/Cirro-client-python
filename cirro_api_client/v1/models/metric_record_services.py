from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MetricRecordServices")


@_attrs_define
class MetricRecordServices:
    """Map of service names to metric value

    Example:
        {'Amazon Simple Storage Service': 24.91}

    """

    additional_properties: dict[str, float] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        metric_record_services = cls()

        metric_record_services.additional_properties = d
        return metric_record_services

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
