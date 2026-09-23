from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.structured_file_input_data_item import StructuredFileInputDataItem


T = TypeVar("T", bound="StructuredFileInput")


@_attrs_define
class StructuredFileInput:
    """Contents for a structured file that a pipeline accepts as an input

    Attributes:
        data (list[StructuredFileInputDataItem]):
        import_source_uris (list[str]):
    """

    data: list[StructuredFileInputDataItem]
    import_source_uris: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        import_source_uris = self.import_source_uris

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "importSourceUris": import_source_uris,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.structured_file_input_data_item import StructuredFileInputDataItem

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = StructuredFileInputDataItem.from_dict(data_item_data)

            data.append(data_item)

        import_source_uris = cast(list[str], d.pop("importSourceUris"))

        structured_file_input = cls(
            data=data,
            import_source_uris=import_source_uris,
        )

        structured_file_input.additional_properties = d
        return structured_file_input

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
