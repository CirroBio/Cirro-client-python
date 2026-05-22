from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskFile")


@_attrs_define
class TaskFile:
    """
    Attributes:
        uri (str): S3 URI of the file
        size (int | None | Unset): File size in bytes
        source_task (str | None | Unset): native_id of the task that produced this file,
            or None if it came from outside the dataset (input files only)
    """

    uri: str
    size: int | None | Unset = UNSET
    source_task: str | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        size: int | None | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        source_task: str | None | Unset
        if isinstance(self.source_task, Unset):
            source_task = UNSET
        else:
            source_task = self.source_task

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({"uri": uri})
        if size is not UNSET:
            field_dict["size"] = size
        if source_task is not UNSET:
            field_dict["sourceTask"] = source_task

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uri = d.pop("uri")

        size_data = d.pop("size", UNSET)
        size: int | None | Unset
        if size_data is None or isinstance(size_data, Unset):
            size = size_data
        else:
            size = int(size_data)

        source_task: str | None | Unset = d.pop("sourceTask", UNSET)

        task_file = cls(uri=uri, size=size, source_task=source_task)
        task_file.additional_properties = d
        return task_file

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
