from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SheetSearchHit")


@_attrs_define
class SheetSearchHit:
    """A distinct value in an indexed column that matched a sheet search, with how many rows hold it

    Attributes:
        sheet_id (str):
        namespace_name (str):
        table_name (str):
        column_name (str):
        value (str): The value as text
        row_count (int): Number of rows whose cell in this column holds the value
    """

    sheet_id: str
    namespace_name: str
    table_name: str
    column_name: str
    value: str
    row_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sheet_id = self.sheet_id

        namespace_name = self.namespace_name

        table_name = self.table_name

        column_name = self.column_name

        value = self.value

        row_count = self.row_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sheetId": sheet_id,
                "namespaceName": namespace_name,
                "tableName": table_name,
                "columnName": column_name,
                "value": value,
                "rowCount": row_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sheet_id = d.pop("sheetId")

        namespace_name = d.pop("namespaceName")

        table_name = d.pop("tableName")

        column_name = d.pop("columnName")

        value = d.pop("value")

        row_count = d.pop("rowCount")

        sheet_search_hit = cls(
            sheet_id=sheet_id,
            namespace_name=namespace_name,
            table_name=table_name,
            column_name=column_name,
            value=value,
            row_count=row_count,
        )

        sheet_search_hit.additional_properties = d
        return sheet_search_hit

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
