from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.row_update_values import RowUpdateValues


T = TypeVar("T", bound="RowUpdate")


@_attrs_define
class RowUpdate:
    """
    Attributes:
        row_id (int): _row_id, which serves as the primary key to identify the row. Example: 42.
        values (RowUpdateValues): Column name and new value. Only the columns included here are updated; all other
            columns on the row are left unchanged. At least one entry is required. Example: {'icd_code': 'G65'}.
    """

    row_id: int
    values: RowUpdateValues
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        row_id = self.row_id

        values = self.values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rowId": row_id,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.row_update_values import RowUpdateValues

        d = dict(src_dict)
        row_id = d.pop("rowId")

        values = RowUpdateValues.from_dict(d.pop("values"))

        row_update = cls(
            row_id=row_id,
            values=values,
        )

        row_update.additional_properties = d
        return row_update

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
