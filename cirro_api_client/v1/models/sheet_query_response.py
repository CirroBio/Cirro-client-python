from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.query_column import QueryColumn
    from ..models.sheet_query_response_rows_item import SheetQueryResponseRowsItem


T = TypeVar("T", bound="SheetQueryResponse")


@_attrs_define
class SheetQueryResponse:
    """
    Attributes:
        columns (list[QueryColumn]):
        rows (list[list[SheetQueryResponseRowsItem]]):
        total_row_count (int):
    """

    columns: list[QueryColumn]
    rows: list[list[SheetQueryResponseRowsItem]]
    total_row_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)

        rows = []
        for rows_item_data in self.rows:
            rows_item = []
            for rows_item_item_data in rows_item_data:
                rows_item_item = rows_item_item_data.to_dict()
                rows_item.append(rows_item_item)

            rows.append(rows_item)

        total_row_count = self.total_row_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columns": columns,
                "rows": rows,
                "totalRowCount": total_row_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_column import QueryColumn
        from ..models.sheet_query_response_rows_item import SheetQueryResponseRowsItem

        d = dict(src_dict)
        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = QueryColumn.from_dict(columns_item_data)

            columns.append(columns_item)

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = []
            _rows_item = rows_item_data
            for rows_item_item_data in _rows_item:
                rows_item_item = SheetQueryResponseRowsItem.from_dict(rows_item_item_data)

                rows_item.append(rows_item_item)

            rows.append(rows_item)

        total_row_count = d.pop("totalRowCount")

        sheet_query_response = cls(
            columns=columns,
            rows=rows,
            total_row_count=total_row_count,
        )

        sheet_query_response.additional_properties = d
        return sheet_query_response

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
