from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.column_mapping import ColumnMapping
    from ..models.entity import Entity


T = TypeVar("T", bound="TargetMapping")


@_attrs_define
class TargetMapping:
    """The saved column mapping from a sheet to one target, such as a pipeline

    Attributes:
        target (Entity):
        column_mappings (list[ColumnMapping]):
    """

    target: Entity
    column_mappings: list[ColumnMapping]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target = self.target.to_dict()

        column_mappings = []
        for column_mappings_item_data in self.column_mappings:
            column_mappings_item = column_mappings_item_data.to_dict()
            column_mappings.append(column_mappings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target": target,
                "columnMappings": column_mappings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.column_mapping import ColumnMapping
        from ..models.entity import Entity

        d = dict(src_dict)
        target = Entity.from_dict(d.pop("target"))

        column_mappings = []
        _column_mappings = d.pop("columnMappings")
        for column_mappings_item_data in _column_mappings:
            column_mappings_item = ColumnMapping.from_dict(column_mappings_item_data)

            column_mappings.append(column_mappings_item)

        target_mapping = cls(
            target=target,
            column_mappings=column_mappings,
        )

        target_mapping.additional_properties = d
        return target_mapping

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
