from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_revision_files import ProcessRevisionFiles


T = TypeVar("T", bound="ProcessRevision")


@_attrs_define
class ProcessRevision:
    """
    Attributes:
        revision_number (int):
        saved_by (str):
        saved_at (datetime.datetime):
        saved_resource_types (list[str]):
        deleted_resource_types (list[str]):
        files (ProcessRevisionFiles):
        commit_message (None | str | Unset):
    """

    revision_number: int
    saved_by: str
    saved_at: datetime.datetime
    saved_resource_types: list[str]
    deleted_resource_types: list[str]
    files: ProcessRevisionFiles
    commit_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revision_number = self.revision_number

        saved_by = self.saved_by

        saved_at = self.saved_at.isoformat()

        saved_resource_types = self.saved_resource_types

        deleted_resource_types = self.deleted_resource_types

        files = self.files.to_dict()

        commit_message: None | str | Unset
        if isinstance(self.commit_message, Unset):
            commit_message = UNSET
        else:
            commit_message = self.commit_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revisionNumber": revision_number,
                "savedBy": saved_by,
                "savedAt": saved_at,
                "savedResourceTypes": saved_resource_types,
                "deletedResourceTypes": deleted_resource_types,
                "files": files,
            }
        )
        if commit_message is not UNSET:
            field_dict["commitMessage"] = commit_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_revision_files import ProcessRevisionFiles

        d = dict(src_dict)
        revision_number = d.pop("revisionNumber")

        saved_by = d.pop("savedBy")

        saved_at = datetime.datetime.fromisoformat(d.pop("savedAt"))

        saved_resource_types = cast(list[str], d.pop("savedResourceTypes"))

        deleted_resource_types = cast(list[str], d.pop("deletedResourceTypes"))

        files = ProcessRevisionFiles.from_dict(d.pop("files"))

        def _parse_commit_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_message = _parse_commit_message(d.pop("commitMessage", UNSET))

        process_revision = cls(
            revision_number=revision_number,
            saved_by=saved_by,
            saved_at=saved_at,
            saved_resource_types=saved_resource_types,
            deleted_resource_types=deleted_resource_types,
            files=files,
            commit_message=commit_message,
        )

        process_revision.additional_properties = d
        return process_revision

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
