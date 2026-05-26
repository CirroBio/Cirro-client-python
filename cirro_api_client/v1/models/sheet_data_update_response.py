from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SheetDataUpdateResponse")


@_attrs_define
class SheetDataUpdateResponse:
    """Data update response for inserts (coming soon), deletes, and updates.

    Attributes:
        rows_affected (int): Number of sheet rows updated (deleted, inserted, updated).
    """

    rows_affected: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rows_affected = self.rows_affected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rowsAffected": rows_affected,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rows_affected = d.pop("rowsAffected")

        sheet_data_update_response = cls(
            rows_affected=rows_affected,
        )

        sheet_data_update_response.additional_properties = d
        return sheet_data_update_response

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
