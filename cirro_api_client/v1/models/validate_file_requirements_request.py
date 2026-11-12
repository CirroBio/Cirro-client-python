from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ValidateFileRequirementsRequest")


@_attrs_define
class ValidateFileRequirementsRequest:
    """
    Attributes:
        sample_sheet (str):
        file_names (list[str]):
    """

    sample_sheet: str
    file_names: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sample_sheet = self.sample_sheet

        file_names = self.file_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sampleSheet": sample_sheet,
                "fileNames": file_names,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sample_sheet = d.pop("sampleSheet")

        file_names = cast(list[str], d.pop("fileNames"))

        validate_file_requirements_request = cls(
            sample_sheet=sample_sheet,
            file_names=file_names,
        )

        validate_file_requirements_request.additional_properties = d
        return validate_file_requirements_request

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
