from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.column_data_type import ColumnDataType
from ..models.semantic_column_type import SemanticColumnType

T = TypeVar("T", bound="ColumnDefSlim")


@_attrs_define
class ColumnDefSlim:
    """
    Attributes:
        name (str):
        data_type (ColumnDataType): Data type for the column.
        semantic_type (SemanticColumnType): The semantic type of the column.
    """

    name: str
    data_type: ColumnDataType
    semantic_type: SemanticColumnType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        data_type = self.data_type.value

        semantic_type = self.semantic_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "dataType": data_type,
                "semanticType": semantic_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        data_type = ColumnDataType(d.pop("dataType"))

        semantic_type = SemanticColumnType(d.pop("semanticType"))

        column_def_slim = cls(
            name=name,
            data_type=data_type,
            semantic_type=semantic_type,
        )

        column_def_slim.additional_properties = d
        return column_def_slim

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
