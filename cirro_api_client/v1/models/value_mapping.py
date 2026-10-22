from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ValueMapping")


@_attrs_define
class ValueMapping:
    """Recodes one source value to a target value, matched exactly. Values are compared as text, so a BOOLEAN or INTEGER
    column matches the value's text form, such as true or 1.

        Attributes:
            source_value (str): Source value; may be empty to recode blank cells Example: Tumor.
            target_value (str): Value the target receives Example: 1.
    """

    source_value: str
    target_value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_value = self.source_value

        target_value = self.target_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceValue": source_value,
                "targetValue": target_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_value = d.pop("sourceValue")

        target_value = d.pop("targetValue")

        value_mapping = cls(
            source_value=source_value,
            target_value=target_value,
        )

        value_mapping.additional_properties = d
        return value_mapping

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
