from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SheetQueryRequest")


@_attrs_define
class SheetQueryRequest:
    """
    Attributes:
        query (str): Raw SQL query to run.
        namespace_name (None | str | Unset): Deprecated: no longer scopes name resolution — every namespace is on the
            engine's search path. Example: default.
        limit (int | None | Unset): Maximum rows to return. Responses also have a size limit: with wide rows a large
            page can fail with a 502 — lower the limit if so. Default: 1000.
        page (int | None | Unset): Page to return Default: 1.
    """

    query: str
    namespace_name: None | str | Unset = UNSET
    limit: int | None | Unset = 1000
    page: int | None | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        namespace_name: None | str | Unset
        if isinstance(self.namespace_name, Unset):
            namespace_name = UNSET
        else:
            namespace_name = self.namespace_name

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        page: int | None | Unset
        if isinstance(self.page, Unset):
            page = UNSET
        else:
            page = self.page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if namespace_name is not UNSET:
            field_dict["namespaceName"] = namespace_name
        if limit is not UNSET:
            field_dict["limit"] = limit
        if page is not UNSET:
            field_dict["page"] = page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        def _parse_namespace_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace_name = _parse_namespace_name(d.pop("namespaceName", UNSET))

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        def _parse_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page = _parse_page(d.pop("page", UNSET))

        sheet_query_request = cls(
            query=query,
            namespace_name=namespace_name,
            limit=limit,
            page=page,
        )

        sheet_query_request.additional_properties = d
        return sheet_query_request

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
