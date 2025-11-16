from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditEventEventDetail")


@_attrs_define
class AuditEventEventDetail:
    """The details of the event, such as the request details sent from the client"""

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        audit_event_event_detail = cls()

        audit_event_event_detail.additional_properties = d
        return audit_event_event_detail

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
