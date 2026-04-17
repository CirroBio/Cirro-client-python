from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.file_def import FileDef


T = TypeVar("T", bound="TriggerIngestRequest")


@_attrs_define
class TriggerIngestRequest:
    """
    Attributes:
        file_def (FileDef): If provided, an ingest job is triggered immediately after table creation (TABLE only)
    """

    file_def: FileDef
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_def = self.file_def.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileDef": file_def,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_def import FileDef

        d = dict(src_dict)
        file_def = FileDef.from_dict(d.pop("fileDef"))

        trigger_ingest_request = cls(
            file_def=file_def,
        )

        trigger_ingest_request.additional_properties = d
        return trigger_ingest_request

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
