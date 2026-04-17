from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="JoinCondition")


@_attrs_define
class JoinCondition:
    """
    Attributes:
        left_column (str): Qualified column reference in alias.column format Example: s1.patient_id.
        right_column (str): Qualified column reference in alias.column format Example: s2.patient_id.
    """

    left_column: str
    right_column: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        left_column = self.left_column

        right_column = self.right_column

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "leftColumn": left_column,
                "rightColumn": right_column,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        left_column = d.pop("leftColumn")

        right_column = d.pop("rightColumn")

        join_condition = cls(
            left_column=left_column,
            right_column=right_column,
        )

        join_condition.additional_properties = d
        return join_condition

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
