from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_mapping import FileMapping
    from ..models.tag import Tag


T = TypeVar("T", bound="CopyDatasetRequest")


@_attrs_define
class CopyDatasetRequest:
    """
    Attributes:
        files (list[FileMapping]): Files and folders to copy into the new dataset, from one or more datasets (at most
            40) or S3 buckets. To copy a whole dataset, give the folder cirro::<projectId>:dataset:<datasetId>/
        run_details_from (None | str | Unset): Cirro URI of a dataset to also copy the run details (params, reports,
            logs) from, cirro::<projectId>:dataset:<datasetId>. It must be one of the datasets files are copied from, and
            needs access to its project, not only through a share
        name (None | str | Unset): Name of the new dataset. Required unless every file comes from one dataset, otherwise
            defaults to that dataset's name
        description (None | str | Unset): Description of the new dataset (defaults to that of the source dataset, when
            every file comes from one)
        tags (list[Tag] | None | Unset): Tags to apply to the new dataset (defaults to those of the source dataset, when
            every file comes from one)
        process_id (None | str | Unset): Type of the new dataset. Defaults to that of runDetailsFrom, or of the source
            datasets if they all have the same type. Required when no file comes from a dataset
        source_dataset_ids (list[str] | None | Unset): IDs of the datasets the new dataset derives from (its lineage),
            e.g. copies in this project of the source datasets' inputs. Each must be in this project. Defaults to the source
            datasets' own sourceDatasetIds
    """

    files: list[FileMapping]
    run_details_from: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    tags: list[Tag] | None | Unset = UNSET
    process_id: None | str | Unset = UNSET
    source_dataset_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        run_details_from: None | str | Unset
        if isinstance(self.run_details_from, Unset):
            run_details_from = UNSET
        else:
            run_details_from = self.run_details_from

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tags: list[dict[str, Any]] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)

        else:
            tags = self.tags

        process_id: None | str | Unset
        if isinstance(self.process_id, Unset):
            process_id = UNSET
        else:
            process_id = self.process_id

        source_dataset_ids: list[str] | None | Unset
        if isinstance(self.source_dataset_ids, Unset):
            source_dataset_ids = UNSET
        elif isinstance(self.source_dataset_ids, list):
            source_dataset_ids = self.source_dataset_ids

        else:
            source_dataset_ids = self.source_dataset_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files": files,
            }
        )
        if run_details_from is not UNSET:
            field_dict["runDetailsFrom"] = run_details_from
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if process_id is not UNSET:
            field_dict["processId"] = process_id
        if source_dataset_ids is not UNSET:
            field_dict["sourceDatasetIds"] = source_dataset_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_mapping import FileMapping
        from ..models.tag import Tag

        d = dict(src_dict)
        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = FileMapping.from_dict(files_item_data)

            files.append(files_item)

        def _parse_run_details_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        run_details_from = _parse_run_details_from(d.pop("runDetailsFrom", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_tags(data: object) -> list[Tag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in _tags_type_0:
                    tags_type_0_item = Tag.from_dict(tags_type_0_item_data)

                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Tag] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_process_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        process_id = _parse_process_id(d.pop("processId", UNSET))

        def _parse_source_dataset_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                source_dataset_ids_type_0 = cast(list[str], data)

                return source_dataset_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        source_dataset_ids = _parse_source_dataset_ids(d.pop("sourceDatasetIds", UNSET))

        copy_dataset_request = cls(
            files=files,
            run_details_from=run_details_from,
            name=name,
            description=description,
            tags=tags,
            process_id=process_id,
            source_dataset_ids=source_dataset_ids,
        )

        copy_dataset_request.additional_properties = d
        return copy_dataset_request

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
