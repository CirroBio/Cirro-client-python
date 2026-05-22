from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.task_file import TaskFile

T = TypeVar("T", bound="TaskFilesResponse")


@_attrs_define
class TaskFilesResponse:
    """
    Attributes:
        input_files (list[TaskFile]): Input files for the task
        output_files (list[TaskFile]): Output files for the task
    """

    input_files: list["TaskFile"]
    output_files: list["TaskFile"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_files = [f.to_dict() for f in self.input_files]
        output_files = [f.to_dict() for f in self.output_files]

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "inputFiles": input_files,
            "outputFiles": output_files,
        })
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_file import TaskFile

        d = dict(src_dict)
        input_files = [TaskFile.from_dict(item) for item in d.pop("inputFiles", [])]
        output_files = [TaskFile.from_dict(item) for item in d.pop("outputFiles", [])]

        obj = cls(input_files=input_files, output_files=output_files)
        obj.additional_properties = d
        return obj

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
