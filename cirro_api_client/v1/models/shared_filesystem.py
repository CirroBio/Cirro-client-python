from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.status import Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.named_item import NamedItem


T = TypeVar("T", bound="SharedFilesystem")


@_attrs_define
class SharedFilesystem:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        project_id (str):
        status (Status):
        created_by (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        status_message (None | str | Unset):
        size_in_bytes (int | None | Unset): Size of file system (refreshed daily)
        warning_threshold_bytes (int | None | Unset):
        used_by_workspaces (list[NamedItem] | Unset): Workspaces currently referencing this filesystem
        used_by_count (int | Unset): Number of workspaces currently referencing this filesystem
    """

    id: str
    name: str
    description: str
    project_id: str
    status: Status
    created_by: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    status_message: None | str | Unset = UNSET
    size_in_bytes: int | None | Unset = UNSET
    warning_threshold_bytes: int | None | Unset = UNSET
    used_by_workspaces: list[NamedItem] | Unset = UNSET
    used_by_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        project_id = self.project_id

        status = self.status.value

        created_by = self.created_by

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        status_message: None | str | Unset
        if isinstance(self.status_message, Unset):
            status_message = UNSET
        else:
            status_message = self.status_message

        size_in_bytes: int | None | Unset
        if isinstance(self.size_in_bytes, Unset):
            size_in_bytes = UNSET
        else:
            size_in_bytes = self.size_in_bytes

        warning_threshold_bytes: int | None | Unset
        if isinstance(self.warning_threshold_bytes, Unset):
            warning_threshold_bytes = UNSET
        else:
            warning_threshold_bytes = self.warning_threshold_bytes

        used_by_workspaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.used_by_workspaces, Unset):
            used_by_workspaces = []
            for used_by_workspaces_item_data in self.used_by_workspaces:
                used_by_workspaces_item = used_by_workspaces_item_data.to_dict()
                used_by_workspaces.append(used_by_workspaces_item)

        used_by_count = self.used_by_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "projectId": project_id,
                "status": status,
                "createdBy": created_by,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message
        if size_in_bytes is not UNSET:
            field_dict["sizeInBytes"] = size_in_bytes
        if warning_threshold_bytes is not UNSET:
            field_dict["warningThresholdBytes"] = warning_threshold_bytes
        if used_by_workspaces is not UNSET:
            field_dict["usedByWorkspaces"] = used_by_workspaces
        if used_by_count is not UNSET:
            field_dict["usedByCount"] = used_by_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.named_item import NamedItem

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        project_id = d.pop("projectId")

        status = Status(d.pop("status"))

        created_by = d.pop("createdBy")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_status_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_message = _parse_status_message(d.pop("statusMessage", UNSET))

        def _parse_size_in_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_in_bytes = _parse_size_in_bytes(d.pop("sizeInBytes", UNSET))

        def _parse_warning_threshold_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        warning_threshold_bytes = _parse_warning_threshold_bytes(d.pop("warningThresholdBytes", UNSET))

        _used_by_workspaces = d.pop("usedByWorkspaces", UNSET)
        used_by_workspaces: list[NamedItem] | Unset = UNSET
        if _used_by_workspaces is not UNSET:
            used_by_workspaces = []
            for used_by_workspaces_item_data in _used_by_workspaces:
                used_by_workspaces_item = NamedItem.from_dict(used_by_workspaces_item_data)

                used_by_workspaces.append(used_by_workspaces_item)

        used_by_count = d.pop("usedByCount", UNSET)

        shared_filesystem = cls(
            id=id,
            name=name,
            description=description,
            project_id=project_id,
            status=status,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            status_message=status_message,
            size_in_bytes=size_in_bytes,
            warning_threshold_bytes=warning_threshold_bytes,
            used_by_workspaces=used_by_workspaces,
            used_by_count=used_by_count,
        )

        shared_filesystem.additional_properties = d
        return shared_filesystem

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
