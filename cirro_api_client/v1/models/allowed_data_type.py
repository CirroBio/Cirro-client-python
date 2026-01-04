from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.file_name_pattern import FileNamePattern


T = TypeVar("T", bound="AllowedDataType")


@_attrs_define
class AllowedDataType:
    """
    Attributes:
        description (str):
        error_msg (str):
        allowed_patterns (List['FileNamePattern']):
    """

    description: str
    error_msg: str
    allowed_patterns: list["FileNamePattern"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        error_msg = self.error_msg

        allowed_patterns = []
        for allowed_patterns_item_data in self.allowed_patterns:
            allowed_patterns_item = allowed_patterns_item_data.to_dict()
            allowed_patterns.append(allowed_patterns_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "errorMsg": error_msg,
                "allowedPatterns": allowed_patterns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.file_name_pattern import FileNamePattern

        d = src_dict.copy()
        description = d.pop("description")

        error_msg = d.pop("errorMsg")

        allowed_patterns = []
        _allowed_patterns = d.pop("allowedPatterns")
        for allowed_patterns_item_data in _allowed_patterns:
            allowed_patterns_item = FileNamePattern.from_dict(allowed_patterns_item_data)

            allowed_patterns.append(allowed_patterns_item)

        allowed_data_type = cls(
            description=description,
            error_msg=error_msg,
            allowed_patterns=allowed_patterns,
        )

        allowed_data_type.additional_properties = d
        return allowed_data_type

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
