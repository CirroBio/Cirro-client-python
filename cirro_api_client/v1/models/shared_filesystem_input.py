from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SharedFilesystemInput")


@_attrs_define
class SharedFilesystemInput:
    """
    Attributes:
        name (str):
        description (None | str | Unset):
        warning_threshold_bytes (int | None | Unset): Size in bytes at which to send a warning notification
    """

    name: str
    description: None | str | Unset = UNSET
    warning_threshold_bytes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        warning_threshold_bytes: int | None | Unset
        if isinstance(self.warning_threshold_bytes, Unset):
            warning_threshold_bytes = UNSET
        else:
            warning_threshold_bytes = self.warning_threshold_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if warning_threshold_bytes is not UNSET:
            field_dict["warningThresholdBytes"] = warning_threshold_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_warning_threshold_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        warning_threshold_bytes = _parse_warning_threshold_bytes(d.pop("warningThresholdBytes", UNSET))

        shared_filesystem_input = cls(
            name=name,
            description=description,
            warning_threshold_bytes=warning_threshold_bytes,
        )

        shared_filesystem_input.additional_properties = d
        return shared_filesystem_input

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
