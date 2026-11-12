from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileMapping")


@_attrs_define
class FileMapping:
    """A file or folder to copy into the new dataset

    Attributes:
        src (str): Cirro URI of a file or folder in the data folder of a dataset in this project or shared with it,
            cirro::<projectId>:dataset:<datasetId>/<path>, or S3 URI of a file or folder in a bucket outside Cirro that the
            project can read, s3://<bucket>/<key>. A path ending in / (or empty) is a folder, and everything under it is
            copied Example: cirro::project-1:dataset:dataset-1/sample1/reads_R1.fastq.gz.
        dest (None | str | Unset): Path in the new dataset's data folder. A folder's destination is a folder (ends in /,
            or empty for the data folder itself). Defaults to the source's path in its dataset, or for an S3 source, the
            data folder itself for a folder and its own name for a file Example: renamed/sample1_R1.fastq.gz.
    """

    src: str
    dest: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        src = self.src

        dest: None | str | Unset
        if isinstance(self.dest, Unset):
            dest = UNSET
        else:
            dest = self.dest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "src": src,
            }
        )
        if dest is not UNSET:
            field_dict["dest"] = dest

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        src = d.pop("src")

        def _parse_dest(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dest = _parse_dest(d.pop("dest", UNSET))

        file_mapping = cls(
            src=src,
            dest=dest,
        )

        file_mapping.additional_properties = d
        return file_mapping

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
