from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.saved_process_revision import SavedProcessRevision


T = TypeVar("T", bound="ProcessRevisionSaveResponse")


@_attrs_define
class ProcessRevisionSaveResponse:
    """
    Attributes:
        files (list[SavedProcessRevision] | Unset): One entry per saved file, in the same order as the request, with the
            resulting URI and content hash.
        current_config_revision (int | Unset): Revision number persisted on the process record after this save.
            Monotonically increasing. Example: 7.
        revision_token (str | Unset): Opaque token for optimistic concurrency. Pass as the If-Match header value on the
            next save; the server returns 412 if another save committed first.
        saved_by (str | Unset): Username of the caller who performed the save.
    """

    files: list[SavedProcessRevision] | Unset = UNSET
    current_config_revision: int | Unset = UNSET
    revision_token: str | Unset = UNSET
    saved_by: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        current_config_revision = self.current_config_revision

        revision_token = self.revision_token

        saved_by = self.saved_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if current_config_revision is not UNSET:
            field_dict["currentConfigRevision"] = current_config_revision
        if revision_token is not UNSET:
            field_dict["revisionToken"] = revision_token
        if saved_by is not UNSET:
            field_dict["savedBy"] = saved_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.saved_process_revision import SavedProcessRevision

        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: list[SavedProcessRevision] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = SavedProcessRevision.from_dict(files_item_data)

                files.append(files_item)

        current_config_revision = d.pop("currentConfigRevision", UNSET)

        revision_token = d.pop("revisionToken", UNSET)

        saved_by = d.pop("savedBy", UNSET)

        process_revision_save_response = cls(
            files=files,
            current_config_revision=current_config_revision,
            revision_token=revision_token,
            saved_by=saved_by,
        )

        process_revision_save_response.additional_properties = d
        return process_revision_save_response

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
