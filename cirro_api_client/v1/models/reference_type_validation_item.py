from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReferenceTypeValidationItem")


@_attrs_define
class ReferenceTypeValidationItem:
    """ """

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reference_type_validation_item = cls()

        reference_type_validation_item.additional_properties = d
        return reference_type_validation_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())
