from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_source import DatasetSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectFile")


@_attrs_define
class ProjectFile:
    """
    Attributes:
        dataset_id (str | Unset): What dataset ID this file originated from
        path (str | Unset): Relative path to file Example: fastq/SRX12875516_SRR16674827_1.fastq.gz.
        absolute_path (str | Unset): Absolute path to file Example:
            s3://project-1a1a/datasets/2a2a/data/fastq/SRX12875516_SRR16674827_1.fastq.gz.
        source (DatasetSource | Unset): How the containing dataset was generated: INGESTED (uploaded) or DERIVED
            (produced by a pipeline)
        process_id (str | Unset): What process created the containing dataset (pipeline or data type)
        file_type (str | Unset): File type derived from the extension, compression suffixes stripped; null when the file
            has no extension Example: fastq.
        size (int | Unset): File size (in bytes) Example: 1435658507.
        created_by (str | Unset): Who created the containing dataset
        created_at (datetime.datetime | Unset): When the file was created
    """

    dataset_id: str | Unset = UNSET
    path: str | Unset = UNSET
    absolute_path: str | Unset = UNSET
    source: DatasetSource | Unset = UNSET
    process_id: str | Unset = UNSET
    file_type: str | Unset = UNSET
    size: int | Unset = UNSET
    created_by: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id = self.dataset_id

        path = self.path

        absolute_path = self.absolute_path

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        process_id = self.process_id

        file_type = self.file_type

        size = self.size

        created_by = self.created_by

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dataset_id is not UNSET:
            field_dict["datasetId"] = dataset_id
        if path is not UNSET:
            field_dict["path"] = path
        if absolute_path is not UNSET:
            field_dict["absolutePath"] = absolute_path
        if source is not UNSET:
            field_dict["source"] = source
        if process_id is not UNSET:
            field_dict["processId"] = process_id
        if file_type is not UNSET:
            field_dict["fileType"] = file_type
        if size is not UNSET:
            field_dict["size"] = size
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_id = d.pop("datasetId", UNSET)

        path = d.pop("path", UNSET)

        absolute_path = d.pop("absolutePath", UNSET)

        _source = d.pop("source", UNSET)
        source: DatasetSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = DatasetSource(_source)

        process_id = d.pop("processId", UNSET)

        file_type = d.pop("fileType", UNSET)

        size = d.pop("size", UNSET)

        created_by = d.pop("createdBy", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        project_file = cls(
            dataset_id=dataset_id,
            path=path,
            absolute_path=absolute_path,
            source=source,
            process_id=process_id,
            file_type=file_type,
            size=size,
            created_by=created_by,
            created_at=created_at,
        )

        project_file.additional_properties = d
        return project_file

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
