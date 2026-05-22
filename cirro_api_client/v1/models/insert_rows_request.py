from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.row_insert import RowInsert


T = TypeVar("T", bound="InsertRowsRequest")


@_attrs_define
class InsertRowsRequest:
    """
    Attributes:
        inserts (list[RowInsert]): List of rows to update.
    """

    inserts: list[RowInsert]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inserts = []
        for inserts_item_data in self.inserts:
            inserts_item = inserts_item_data.to_dict()
            inserts.append(inserts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inserts": inserts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.row_insert import RowInsert

        d = dict(src_dict)
        inserts = []
        _inserts = d.pop("inserts")
        for inserts_item_data in _inserts:
            inserts_item = RowInsert.from_dict(inserts_item_data)

            inserts.append(inserts_item)

        insert_rows_request = cls(
            inserts=inserts,
        )

        insert_rows_request.additional_properties = d
        return insert_rows_request

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
