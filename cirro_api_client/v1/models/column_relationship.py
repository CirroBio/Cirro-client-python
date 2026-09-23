from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ColumnRelationship")


@_attrs_define
class ColumnRelationship:
    """A foreign-key relationship from a column in this sheet to a column in another sheet.

    Attributes:
        column_name (str): Name of the foreign-key column on this sheet.
        target_sheet_id (str): ID of the sheet this relationship references.
        target_column_name (str): Name of the referenced column in the target sheet.
    """

    column_name: str
    target_sheet_id: str
    target_column_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column_name = self.column_name

        target_sheet_id = self.target_sheet_id

        target_column_name = self.target_column_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columnName": column_name,
                "targetSheetId": target_sheet_id,
                "targetColumnName": target_column_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        column_name = d.pop("columnName")

        target_sheet_id = d.pop("targetSheetId")

        target_column_name = d.pop("targetColumnName")

        column_relationship = cls(
            column_name=column_name,
            target_sheet_id=target_sheet_id,
            target_column_name=target_column_name,
        )

        column_relationship.additional_properties = d
        return column_relationship

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
