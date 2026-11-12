from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sheet_row_change_type import SheetRowChangeType

T = TypeVar("T", bound="SheetRowChange")


@_attrs_define
class SheetRowChange:
    """A row that changed between two snapshots.

    Attributes:
        row_id (int): The row's `_row_id`, which an update keeps.
        change (SheetRowChangeType): How a row changed between two snapshots.
    """

    row_id: int
    change: SheetRowChangeType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        row_id = self.row_id

        change = self.change.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rowId": row_id,
                "change": change,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        row_id = d.pop("rowId")

        change = SheetRowChangeType(d.pop("change"))

        sheet_row_change = cls(
            row_id=row_id,
            change=change,
        )

        sheet_row_change.additional_properties = d
        return sheet_row_change

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
