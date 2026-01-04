from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MountedDataset")


@_attrs_define
class MountedDataset:
    """Represents a mounted dataset in a workspace

    Attributes:
        name (str): Folder name that appears in the workspace
        uri (str): Full S3 prefix to the data
    """

    name: str
    uri: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        uri = d.pop("uri")

        mounted_dataset = cls(
            name=name,
            uri=uri,
        )

        mounted_dataset.additional_properties = d
        return mounted_dataset

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
