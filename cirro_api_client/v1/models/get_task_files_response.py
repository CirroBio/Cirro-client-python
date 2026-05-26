from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.file_entry import FileEntry


T = TypeVar("T", bound="GetTaskFilesResponse")


@_attrs_define
class GetTaskFilesResponse:
    """
    Attributes:
        input_files (list[FileEntry]):
        output_files (list[FileEntry]):
    """

    input_files: list[FileEntry]
    output_files: list[FileEntry]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_files = []
        for input_files_item_data in self.input_files:
            input_files_item = input_files_item_data.to_dict()
            input_files.append(input_files_item)

        output_files = []
        for output_files_item_data in self.output_files:
            output_files_item = output_files_item_data.to_dict()
            output_files.append(output_files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inputFiles": input_files,
                "outputFiles": output_files,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_entry import FileEntry

        d = dict(src_dict)
        input_files = []
        _input_files = d.pop("inputFiles")
        for input_files_item_data in _input_files:
            input_files_item = FileEntry.from_dict(input_files_item_data)

            input_files.append(input_files_item)

        output_files = []
        _output_files = d.pop("outputFiles")
        for output_files_item_data in _output_files:
            output_files_item = FileEntry.from_dict(output_files_item_data)

            output_files.append(output_files_item)

        get_task_files_response = cls(
            input_files=input_files,
            output_files=output_files,
        )

        get_task_files_response.additional_properties = d
        return get_task_files_response

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
