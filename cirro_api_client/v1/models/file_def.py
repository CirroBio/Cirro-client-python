from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_type import FileType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileDef")


@_attrs_define
class FileDef:
    """If provided, an ingest job is triggered immediately after table creation (TABLE only)

    Attributes:
        file_type (FileType):
        storage_uri (str | Unset): Full S3 URI to the source file.
    """

    file_type: FileType
    storage_uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_type = self.file_type.value

        storage_uri = self.storage_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileType": file_type,
            }
        )
        if storage_uri is not UNSET:
            field_dict["storageUri"] = storage_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_type = FileType(d.pop("fileType"))

        storage_uri = d.pop("storageUri", UNSET)

        file_def = cls(
            file_type=file_type,
            storage_uri=storage_uri,
        )

        file_def.additional_properties = d
        return file_def

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
