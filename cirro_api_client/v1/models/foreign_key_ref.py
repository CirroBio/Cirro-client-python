from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ForeignKeyRef")


@_attrs_define
class ForeignKeyRef:
    """
    Attributes:
        sheet_id (str):
        column_name (str):
    """

    sheet_id: str
    column_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sheet_id = self.sheet_id

        column_name = self.column_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sheetId": sheet_id,
                "columnName": column_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sheet_id = d.pop("sheetId")

        column_name = d.pop("columnName")

        foreign_key_ref = cls(
            sheet_id=sheet_id,
            column_name=column_name,
        )

        foreign_key_ref.additional_properties = d
        return foreign_key_ref

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
