from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MountedDataset")


@_attrs_define
class MountedDataset:
    """Represents a mounted dataset in a workspace

    Attributes:
        name (str): Folder name that appears in the workspace
        dataset_id (None | str | Unset): ID of the dataset to mount
        custom_uri (None | str | Unset): Full S3 URI to mounted data (if mounting custom path)
    """

    name: str
    dataset_id: None | str | Unset = UNSET
    custom_uri: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        dataset_id: None | str | Unset
        if isinstance(self.dataset_id, Unset):
            dataset_id = UNSET
        else:
            dataset_id = self.dataset_id

        custom_uri: None | str | Unset
        if isinstance(self.custom_uri, Unset):
            custom_uri = UNSET
        else:
            custom_uri = self.custom_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if dataset_id is not UNSET:
            field_dict["datasetId"] = dataset_id
        if custom_uri is not UNSET:
            field_dict["customUri"] = custom_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_dataset_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_id = _parse_dataset_id(d.pop("datasetId", UNSET))

        def _parse_custom_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_uri = _parse_custom_uri(d.pop("customUri", UNSET))

        mounted_dataset = cls(
            name=name,
            dataset_id=dataset_id,
            custom_uri=custom_uri,
        )

        mounted_dataset.additional_properties = d
        return mounted_dataset

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
