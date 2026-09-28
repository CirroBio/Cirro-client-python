from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_task_lineage_response_lineage import GetTaskLineageResponseLineage


T = TypeVar("T", bound="GetTaskLineageResponse")


@_attrs_define
class GetTaskLineageResponse:
    """
    Attributes:
        lineage (GetTaskLineageResponseLineage | Unset): Lineage specific to the executor
    """

    lineage: GetTaskLineageResponseLineage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lineage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lineage, Unset):
            lineage = self.lineage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lineage is not UNSET:
            field_dict["lineage"] = lineage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_task_lineage_response_lineage import GetTaskLineageResponseLineage

        d = dict(src_dict)
        _lineage = d.pop("lineage", UNSET)
        lineage: GetTaskLineageResponseLineage | Unset
        if isinstance(_lineage, Unset):
            lineage = UNSET
        else:
            lineage = GetTaskLineageResponseLineage.from_dict(_lineage)

        get_task_lineage_response = cls(
            lineage=lineage,
        )

        get_task_lineage_response.additional_properties = d
        return get_task_lineage_response

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
