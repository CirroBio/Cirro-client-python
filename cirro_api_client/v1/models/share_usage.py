from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status import Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity import Entity


T = TypeVar("T", bound="ShareUsage")


@_attrs_define
class ShareUsage:
    """Record of a consuming item has been granted access to a dataset via a share.

    Attributes:
        id (str):
        consuming_item (Entity):
        updated_at (datetime.datetime):
        consuming_project_id (str | Unset): ID of the project the consuming item belongs to.
        originating_dataset_id (str | Unset): ID of the dataset in the originating project that was shared.
        status (Status | Unset): Current state of the usage. RUNNING means access is active; DELETED means the access
            point has been revoked.
        access_point_arn (str | Unset): ARN of the shared AWS S3 access point. One access point covers all usages from
            the same consuming item to the same originating project.
        created_at (datetime.datetime | Unset): When access was first granted.
    """

    id: str
    consuming_item: Entity
    updated_at: datetime.datetime
    consuming_project_id: str | Unset = UNSET
    originating_dataset_id: str | Unset = UNSET
    status: Status | Unset = UNSET
    access_point_arn: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        consuming_item = self.consuming_item.to_dict()

        updated_at = self.updated_at.isoformat()

        consuming_project_id = self.consuming_project_id

        originating_dataset_id = self.originating_dataset_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        access_point_arn = self.access_point_arn

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "consumingItem": consuming_item,
                "updatedAt": updated_at,
            }
        )
        if consuming_project_id is not UNSET:
            field_dict["consumingProjectId"] = consuming_project_id
        if originating_dataset_id is not UNSET:
            field_dict["originatingDatasetId"] = originating_dataset_id
        if status is not UNSET:
            field_dict["status"] = status
        if access_point_arn is not UNSET:
            field_dict["accessPointArn"] = access_point_arn
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity import Entity

        d = dict(src_dict)
        id = d.pop("id")

        consuming_item = Entity.from_dict(d.pop("consumingItem"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        consuming_project_id = d.pop("consumingProjectId", UNSET)

        originating_dataset_id = d.pop("originatingDatasetId", UNSET)

        _status = d.pop("status", UNSET)
        status: Status | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Status(_status)

        access_point_arn = d.pop("accessPointArn", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        share_usage = cls(
            id=id,
            consuming_item=consuming_item,
            updated_at=updated_at,
            consuming_project_id=consuming_project_id,
            originating_dataset_id=originating_dataset_id,
            status=status,
            access_point_arn=access_point_arn,
            created_at=created_at,
        )

        share_usage.additional_properties = d
        return share_usage

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
