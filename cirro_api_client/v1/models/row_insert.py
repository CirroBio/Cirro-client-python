from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.row_insert_values import RowInsertValues


T = TypeVar("T", bound="RowInsert")


@_attrs_define
class RowInsert:
    """
    Attributes:
        values (RowInsertValues): Column name and value. Any missing columns will have a null value (will error if
            column is required). Cirro-typed columns hold Cirro URIs of the form
            cirro:<tenantId>:<projectId>:dataset:<datasetId>/<path> (scope segments may be empty; path relative to the
            dataset's data directory). CIRRO_DATASET cells reference the dataset itself and have no path. Example:
            {'icd_code': 'G65', 'sample_file': 'cirro::1a1a...:dataset:d4f1.../results/sample1.fastq.gz'}.
    """

    values: RowInsertValues
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        values = self.values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.row_insert_values import RowInsertValues

        d = dict(src_dict)
        values = RowInsertValues.from_dict(d.pop("values"))

        row_insert = cls(
            values=values,
        )

        row_insert.additional_properties = d
        return row_insert

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
