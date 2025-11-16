from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.data_file_metadata import DataFileMetadata


T = TypeVar("T", bound="DataFile")


@_attrs_define
class DataFile:
    """
    Attributes:
        path (str):
        metadata (DataFileMetadata):
    """

    path: str
    metadata: "DataFileMetadata"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_file_metadata import DataFileMetadata

        d = src_dict.copy()
        path = d.pop("path")

        metadata = DataFileMetadata.from_dict(d.pop("metadata"))

        data_file = cls(
            path=path,
            metadata=metadata,
        )

        data_file.additional_properties = d
        return data_file

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
