from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_format import FileFormat

if TYPE_CHECKING:
    from ..models.structured_input_data_item import StructuredInputDataItem


T = TypeVar("T", bound="StructuredInput")


@_attrs_define
class StructuredInput:
    """Contents for a structured file that a pipeline accepts as an input

    Attributes:
        data (list[StructuredInputDataItem]):
        file_format (FileFormat): Determines the file format used when passing the schema-validated input to the
            pipeline.
             - CSV: comma-delimited, one row per object, header row taken from the order properties first appear in the
            rows.
               Nested objects/arrays within a row are JSON-encoded inline as a single cell value (not recommended).
             - TSV: same as CSV, but tab-delimited.
             - JSON: the row objects are written out unmodified as a JSON array (no flattening).
        import_source_uris (list[str]):
    """

    data: list[StructuredInputDataItem]
    file_format: FileFormat
    import_source_uris: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        file_format = self.file_format.value

        import_source_uris = self.import_source_uris

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "fileFormat": file_format,
                "importSourceUris": import_source_uris,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.structured_input_data_item import StructuredInputDataItem

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = StructuredInputDataItem.from_dict(data_item_data)

            data.append(data_item)

        file_format = FileFormat(d.pop("fileFormat"))

        import_source_uris = cast(list[str], d.pop("importSourceUris"))

        structured_input = cls(
            data=data,
            file_format=file_format,
            import_source_uris=import_source_uris,
        )

        structured_input.additional_properties = d
        return structured_input

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
