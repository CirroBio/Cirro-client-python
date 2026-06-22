from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessDocumentation")


@_attrs_define
class ProcessDocumentation:
    """
    Attributes:
        docs_uri (None | str | Unset): Full URI to documentation
        partial_uri (None | str | Unset): URI of process documentation (partial) - only for Cirro-hosted docs
        content (None | str | Unset): Documentation content
    """

    docs_uri: None | str | Unset = UNSET
    partial_uri: None | str | Unset = UNSET
    content: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        docs_uri: None | str | Unset
        if isinstance(self.docs_uri, Unset):
            docs_uri = UNSET
        else:
            docs_uri = self.docs_uri

        partial_uri: None | str | Unset
        if isinstance(self.partial_uri, Unset):
            partial_uri = UNSET
        else:
            partial_uri = self.partial_uri

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if docs_uri is not UNSET:
            field_dict["docsUri"] = docs_uri
        if partial_uri is not UNSET:
            field_dict["partialUri"] = partial_uri
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_docs_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        docs_uri = _parse_docs_uri(d.pop("docsUri", UNSET))

        def _parse_partial_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        partial_uri = _parse_partial_uri(d.pop("partialUri", UNSET))

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        process_documentation = cls(
            docs_uri=docs_uri,
            partial_uri=partial_uri,
            content=content,
        )

        process_documentation.additional_properties = d
        return process_documentation

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
