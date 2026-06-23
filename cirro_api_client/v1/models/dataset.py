from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status import Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tag import Tag


T = TypeVar("T", bound="Dataset")


@_attrs_define
class Dataset:
    """
    Attributes:
        id (str): Dataset ID
        name (str): Dataset name
        project_id (str): Project ID
        process_id (str): Process ID
        source_dataset_ids (list[str]): Source dataset IDs
        status (Status):
        tags (list[Tag]): Tags
        created_by (str): User who created the dataset
        created_at (datetime.datetime): Timestamp when the dataset was created
        updated_at (datetime.datetime): Timestamp when the dataset was last updated
        description (str | Unset): Dataset description
    """

    id: str
    name: str
    project_id: str
    process_id: str
    source_dataset_ids: list[str]
    status: Status
    tags: list[Tag]
    created_by: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        project_id = self.project_id

        process_id = self.process_id

        source_dataset_ids = self.source_dataset_ids

        status = self.status.value

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        created_by = self.created_by

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "projectId": project_id,
                "processId": process_id,
                "sourceDatasetIds": source_dataset_ids,
                "status": status,
                "tags": tags,
                "createdBy": created_by,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tag import Tag

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        project_id = d.pop("projectId")

        process_id = d.pop("processId")

        source_dataset_ids = cast(list[str], d.pop("sourceDatasetIds"))

        status = Status(d.pop("status"))

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = Tag.from_dict(tags_item_data)

            tags.append(tags_item)

        created_by = d.pop("createdBy")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        description = d.pop("description", UNSET)

        dataset = cls(
            id=id,
            name=name,
            project_id=project_id,
            process_id=process_id,
            source_dataset_ids=source_dataset_ids,
            status=status,
            tags=tags,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
        )

        dataset.additional_properties = d
        return dataset

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
