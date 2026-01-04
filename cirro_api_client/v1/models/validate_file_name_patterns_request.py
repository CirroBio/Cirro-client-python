from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ValidateFileNamePatternsRequest")


@_attrs_define
class ValidateFileNamePatternsRequest:
    """
    Attributes:
        file_names (List[str]):
        file_name_patterns (List[str]):
    """

    file_names: list[str]
    file_name_patterns: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_names = self.file_names

        file_name_patterns = self.file_name_patterns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileNames": file_names,
                "fileNamePatterns": file_name_patterns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        file_names = cast(list[str], d.pop("fileNames"))

        file_name_patterns = cast(list[str], d.pop("fileNamePatterns"))

        validate_file_name_patterns_request = cls(
            file_names=file_names,
            file_name_patterns=file_name_patterns,
        )

        validate_file_name_patterns_request.additional_properties = d
        return validate_file_name_patterns_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
