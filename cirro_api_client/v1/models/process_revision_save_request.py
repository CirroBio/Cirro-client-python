from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_resource import ProcessResource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_revision_save_file import ProcessRevisionSaveFile


T = TypeVar("T", bound="ProcessRevisionSaveRequest")


@_attrs_define
class ProcessRevisionSaveRequest:
    """
    Attributes:
        files (list[ProcessRevisionSaveFile] | None | Unset): Files to persist in this revision; one entry per resource
            type. May be omitted when only deletions are requested.
        deleted_resource_types (list[ProcessResource] | None | Unset): Resource types to remove from the new revision's
            snapshot. Underlying S3 content is never deleted; prior revisions retain their references.
        commit_message (None | str | Unset): Optional human-readable note describing the change. Maximum 1024
            characters.
    """

    files: list[ProcessRevisionSaveFile] | None | Unset = UNSET
    deleted_resource_types: list[ProcessResource] | None | Unset = UNSET
    commit_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files: list[dict[str, Any]] | None | Unset
        if isinstance(self.files, Unset):
            files = UNSET
        elif isinstance(self.files, list):
            files = []
            for files_type_0_item_data in self.files:
                files_type_0_item = files_type_0_item_data.to_dict()
                files.append(files_type_0_item)

        else:
            files = self.files

        deleted_resource_types: list[str] | None | Unset
        if isinstance(self.deleted_resource_types, Unset):
            deleted_resource_types = UNSET
        elif isinstance(self.deleted_resource_types, list):
            deleted_resource_types = []
            for deleted_resource_types_type_0_item_data in self.deleted_resource_types:
                deleted_resource_types_type_0_item = deleted_resource_types_type_0_item_data.value
                deleted_resource_types.append(deleted_resource_types_type_0_item)

        else:
            deleted_resource_types = self.deleted_resource_types

        commit_message: None | str | Unset
        if isinstance(self.commit_message, Unset):
            commit_message = UNSET
        else:
            commit_message = self.commit_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if deleted_resource_types is not UNSET:
            field_dict["deletedResourceTypes"] = deleted_resource_types
        if commit_message is not UNSET:
            field_dict["commitMessage"] = commit_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_revision_save_file import ProcessRevisionSaveFile

        d = dict(src_dict)

        def _parse_files(data: object) -> list[ProcessRevisionSaveFile] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                files_type_0 = []
                _files_type_0 = data
                for files_type_0_item_data in _files_type_0:
                    files_type_0_item = ProcessRevisionSaveFile.from_dict(files_type_0_item_data)

                    files_type_0.append(files_type_0_item)

                return files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProcessRevisionSaveFile] | None | Unset, data)

        files = _parse_files(d.pop("files", UNSET))

        def _parse_deleted_resource_types(data: object) -> list[ProcessResource] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                deleted_resource_types_type_0 = []
                _deleted_resource_types_type_0 = data
                for deleted_resource_types_type_0_item_data in _deleted_resource_types_type_0:
                    deleted_resource_types_type_0_item = ProcessResource(deleted_resource_types_type_0_item_data)

                    deleted_resource_types_type_0.append(deleted_resource_types_type_0_item)

                return deleted_resource_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProcessResource] | None | Unset, data)

        deleted_resource_types = _parse_deleted_resource_types(d.pop("deletedResourceTypes", UNSET))

        def _parse_commit_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_message = _parse_commit_message(d.pop("commitMessage", UNSET))

        process_revision_save_request = cls(
            files=files,
            deleted_resource_types=deleted_resource_types,
            commit_message=commit_message,
        )

        process_revision_save_request.additional_properties = d
        return process_revision_save_request

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
