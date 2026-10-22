from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allowed_data_type import AllowedDataType
    from ..models.sheet_template import SheetTemplate


T = TypeVar("T", bound="FileRequirements")


@_attrs_define
class FileRequirements:
    """
    Attributes:
        files (list[str]):
        error_msg (str):
        allowed_data_types (list[AllowedDataType]):
        sheet_template (None | SheetTemplate | Unset):
        has_error (bool | Unset):
    """

    files: list[str]
    error_msg: str
    allowed_data_types: list[AllowedDataType]
    sheet_template: None | SheetTemplate | Unset = UNSET
    has_error: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sheet_template import SheetTemplate

        files = self.files

        error_msg = self.error_msg

        allowed_data_types = []
        for allowed_data_types_item_data in self.allowed_data_types:
            allowed_data_types_item = allowed_data_types_item_data.to_dict()
            allowed_data_types.append(allowed_data_types_item)

        sheet_template: dict[str, Any] | None | Unset
        if isinstance(self.sheet_template, Unset):
            sheet_template = UNSET
        elif isinstance(self.sheet_template, SheetTemplate):
            sheet_template = self.sheet_template.to_dict()
        else:
            sheet_template = self.sheet_template

        has_error = self.has_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files": files,
                "errorMsg": error_msg,
                "allowedDataTypes": allowed_data_types,
            }
        )
        if sheet_template is not UNSET:
            field_dict["sheetTemplate"] = sheet_template
        if has_error is not UNSET:
            field_dict["hasError"] = has_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allowed_data_type import AllowedDataType
        from ..models.sheet_template import SheetTemplate

        d = dict(src_dict)
        files = cast(list[str], d.pop("files"))

        error_msg = d.pop("errorMsg")

        allowed_data_types = []
        _allowed_data_types = d.pop("allowedDataTypes")
        for allowed_data_types_item_data in _allowed_data_types:
            allowed_data_types_item = AllowedDataType.from_dict(allowed_data_types_item_data)

            allowed_data_types.append(allowed_data_types_item)

        def _parse_sheet_template(data: object) -> None | SheetTemplate | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sheet_template_type_1 = SheetTemplate.from_dict(data)

                return sheet_template_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SheetTemplate | Unset, data)

        sheet_template = _parse_sheet_template(d.pop("sheetTemplate", UNSET))

        has_error = d.pop("hasError", UNSET)

        file_requirements = cls(
            files=files,
            error_msg=error_msg,
            allowed_data_types=allowed_data_types,
            sheet_template=sheet_template,
            has_error=has_error,
        )

        file_requirements.additional_properties = d
        return file_requirements

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
