from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditEventEventDetailType0")


@_attrs_define
class AuditEventEventDetailType0:
    """The details of the event, such as the request details sent from the client"""

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        audit_event_event_detail_type_0 = cls()

        audit_event_event_detail_type_0.additional_properties = d
        return audit_event_event_detail_type_0

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())
