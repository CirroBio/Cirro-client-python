from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.value_mapping import ValueMapping


T = TypeVar("T", bound="ColumnMapping")


@_attrs_define
class ColumnMapping:
    """One source column feeding one column of the target. A target column listed more than once, from different source
    columns, has alternatives; one is used per run.

        Attributes:
            source_column (str): Source column, matched case-insensitively and returned in the source's spelling Example:
                read_1.
            target_column (str): Column of the target it feeds Example: fastq_1.
            transform (None | str | Unset): Applied to each source value before the value mappings. Refers to the source
                value as "value", never by column name, so it survives column renames. Stored as given; the portal defines the
                rest of its syntax. Example: =TRIM(value).
            value_mappings (list[ValueMapping] | None | Unset): Recodes values before they reach the target. A value with no
                entry passes through unchanged.
    """

    source_column: str
    target_column: str
    transform: None | str | Unset = UNSET
    value_mappings: list[ValueMapping] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_column = self.source_column

        target_column = self.target_column

        transform: None | str | Unset
        if isinstance(self.transform, Unset):
            transform = UNSET
        else:
            transform = self.transform

        value_mappings: list[dict[str, Any]] | None | Unset
        if isinstance(self.value_mappings, Unset):
            value_mappings = UNSET
        elif isinstance(self.value_mappings, list):
            value_mappings = []
            for value_mappings_type_0_item_data in self.value_mappings:
                value_mappings_type_0_item = value_mappings_type_0_item_data.to_dict()
                value_mappings.append(value_mappings_type_0_item)

        else:
            value_mappings = self.value_mappings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceColumn": source_column,
                "targetColumn": target_column,
            }
        )
        if transform is not UNSET:
            field_dict["transform"] = transform
        if value_mappings is not UNSET:
            field_dict["valueMappings"] = value_mappings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.value_mapping import ValueMapping

        d = dict(src_dict)
        source_column = d.pop("sourceColumn")

        target_column = d.pop("targetColumn")

        def _parse_transform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transform = _parse_transform(d.pop("transform", UNSET))

        def _parse_value_mappings(data: object) -> list[ValueMapping] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_mappings_type_0 = []
                _value_mappings_type_0 = data
                for value_mappings_type_0_item_data in _value_mappings_type_0:
                    value_mappings_type_0_item = ValueMapping.from_dict(value_mappings_type_0_item_data)

                    value_mappings_type_0.append(value_mappings_type_0_item)

                return value_mappings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ValueMapping] | None | Unset, data)

        value_mappings = _parse_value_mappings(d.pop("valueMappings", UNSET))

        column_mapping = cls(
            source_column=source_column,
            target_column=target_column,
            transform=transform,
            value_mappings=value_mappings,
        )

        column_mapping.additional_properties = d
        return column_mapping

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
