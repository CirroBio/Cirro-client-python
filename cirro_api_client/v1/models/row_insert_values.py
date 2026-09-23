from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RowInsertValues")


@_attrs_define
class RowInsertValues:
    """Column name and value. Any missing columns will have a null value (will error if column is required). Cirro-typed
    columns hold Cirro URIs of the form cirro:<tenantId>:<projectId>:data:<datasetId>/<path> (scope segments may be
    empty; path relative to the dataset's data directory). CIRRO_DATASET cells reference the dataset itself and have no
    path.

        Example:
            {'icd_code': 'G65', 'sample_file': 'cirro::1a1a...:data:d4f1.../results/sample1.fastq.gz'}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        row_insert_values = cls()

        row_insert_values.additional_properties = d
        return row_insert_values

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
