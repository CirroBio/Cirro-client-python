from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_resource import ProcessResource
from ..types import UNSET, Unset

T = TypeVar("T", bound="SavedProcessRevision")


@_attrs_define
class SavedProcessRevision:
    """
    Attributes:
        type_ (ProcessResource | Unset): Resource type for this saved file. Example: FORM.
        uri (str | Unset): S3 URI of the content-addressed object written for this resource. Example: s3://tenant-
            resources-bucket/process/user/alice/my-pipeline/config/storage/form/3a7bd3....
        content_sha_256 (str | Unset): Hex-encoded SHA-256 of the file content. Also used as the leaf segment of the S3
            key. Example: 3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b.
    """

    type_: ProcessResource | Unset = UNSET
    uri: str | Unset = UNSET
    content_sha_256: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        uri = self.uri

        content_sha_256 = self.content_sha_256

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uri is not UNSET:
            field_dict["uri"] = uri
        if content_sha_256 is not UNSET:
            field_dict["contentSha256"] = content_sha_256

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

        uri = d.pop("uri", UNSET)

        content_sha_256 = d.pop("contentSha256", UNSET)

        saved_process_revision = cls(
            type_=type_,
            uri=uri,
            content_sha_256=content_sha_256,
        )

        saved_process_revision.additional_properties = d
        return saved_process_revision

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
