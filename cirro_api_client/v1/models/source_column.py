from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceColumn")


@_attrs_define
class SourceColumn:
    """
    Attributes:
        sheet_column (str):
        file_column (None | str | Unset): File column header name. Use this OR index, not both.
        index (int | None | Unset): 0-based file column position. Use this OR fileColumn, not both.
    """

    sheet_column: str
    file_column: None | str | Unset = UNSET
    index: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sheet_column = self.sheet_column

        file_column: None | str | Unset
        if isinstance(self.file_column, Unset):
            file_column = UNSET
        else:
            file_column = self.file_column

        index: int | None | Unset
        if isinstance(self.index, Unset):
            index = UNSET
        else:
            index = self.index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sheetColumn": sheet_column,
            }
        )
        if file_column is not UNSET:
            field_dict["fileColumn"] = file_column
        if index is not UNSET:
            field_dict["index"] = index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sheet_column = d.pop("sheetColumn")

        def _parse_file_column(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_column = _parse_file_column(d.pop("fileColumn", UNSET))

        def _parse_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        index = _parse_index(d.pop("index", UNSET))

        source_column = cls(
            sheet_column=sheet_column,
            file_column=file_column,
            index=index,
        )

        source_column.additional_properties = d
        return source_column

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
