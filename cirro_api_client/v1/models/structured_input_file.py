from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StructuredInputFile")


@_attrs_define
class StructuredInputFile:
    """Record of a structured file used as an input to the pipeline

    Attributes:
        name (str | Unset): Name of the input file
        path (str | Unset): Path to raw input data in JSON format
        serialized_path (str | Unset): Path to file passed into the pipeline
    """

    name: str | Unset = UNSET
    path: str | Unset = UNSET
    serialized_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        path = self.path

        serialized_path = self.serialized_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if serialized_path is not UNSET:
            field_dict["serializedPath"] = serialized_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        path = d.pop("path", UNSET)

        serialized_path = d.pop("serializedPath", UNSET)

        structured_input_file = cls(
            name=name,
            path=path,
            serialized_path=serialized_path,
        )

        structured_input_file.additional_properties = d
        return structured_input_file

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
