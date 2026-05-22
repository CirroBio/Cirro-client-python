from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_def import FileDef
    from ..models.source_column import SourceColumn


T = TypeVar("T", bound="SheetIngestRequest")


@_attrs_define
class SheetIngestRequest:
    """
    Attributes:
        file_def (FileDef):
        source_columns (list[SourceColumn] | None | Unset): List of file column to sheet column mapping. If null,
            requires the column headers to match the sheet column names.
    """

    file_def: FileDef
    source_columns: list[SourceColumn] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_def = self.file_def.to_dict()

        source_columns: list[dict[str, Any]] | None | Unset
        if isinstance(self.source_columns, Unset):
            source_columns = UNSET
        elif isinstance(self.source_columns, list):
            source_columns = []
            for source_columns_type_0_item_data in self.source_columns:
                source_columns_type_0_item = source_columns_type_0_item_data.to_dict()
                source_columns.append(source_columns_type_0_item)

        else:
            source_columns = self.source_columns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileDef": file_def,
            }
        )
        if source_columns is not UNSET:
            field_dict["sourceColumns"] = source_columns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_def import FileDef
        from ..models.source_column import SourceColumn

        d = dict(src_dict)
        file_def = FileDef.from_dict(d.pop("fileDef"))

        def _parse_source_columns(data: object) -> list[SourceColumn] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                source_columns_type_0 = []
                _source_columns_type_0 = data
                for source_columns_type_0_item_data in _source_columns_type_0:
                    source_columns_type_0_item = SourceColumn.from_dict(source_columns_type_0_item_data)

                    source_columns_type_0.append(source_columns_type_0_item)

                return source_columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SourceColumn] | None | Unset, data)

        source_columns = _parse_source_columns(d.pop("sourceColumns", UNSET))

        sheet_ingest_request = cls(
            file_def=file_def,
            source_columns=source_columns,
        )

        sheet_ingest_request.additional_properties = d
        return sheet_ingest_request

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
