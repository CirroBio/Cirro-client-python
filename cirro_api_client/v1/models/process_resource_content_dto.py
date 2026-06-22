from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_resource import ProcessResource
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessResourceContentDto")


@_attrs_define
class ProcessResourceContentDto:
    """Stored content for a single pipeline configuration resource at the current revision.

    Attributes:
        type_ (ProcessResource | Unset): Resource type for this saved file. Example: FORM.
        revision_number (int | Unset): The revision number this content was read from (the latest revision of the
            process at request time).
        digest (str | Unset): Sha256 hex of the content bytes. Matches the entry in the revision's files map. Same value
            appears in the response ETag header.
        content (str | Unset): Raw resource content as a string. For JSON-typed resources this is a serialized JSON
            document.
    """

    type_: ProcessResource | Unset = UNSET
    revision_number: int | Unset = UNSET
    digest: str | Unset = UNSET
    content: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        revision_number = self.revision_number

        digest = self.digest

        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if revision_number is not UNSET:
            field_dict["revisionNumber"] = revision_number
        if digest is not UNSET:
            field_dict["digest"] = digest
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: ProcessResource | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ProcessResource(_type_)

        revision_number = d.pop("revisionNumber", UNSET)

        digest = d.pop("digest", UNSET)

        content = d.pop("content", UNSET)

        process_resource_content_dto = cls(
            type_=type_,
            revision_number=revision_number,
            digest=digest,
            content=content,
        )

        process_resource_content_dto.additional_properties = d
        return process_resource_content_dto

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
