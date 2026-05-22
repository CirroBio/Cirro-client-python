from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_ import Filter
    from ..models.sheet_sort import SheetSort


T = TypeVar("T", bound="SheetDataRequest")


@_attrs_define
class SheetDataRequest:
    """Paginated sheet data query with optional sort and filter

    Attributes:
        limit (int | None | Unset): Maximum rows to return Default: 1000.
        page (int | None | Unset): Page to return Default: 1.
        sort (None | SheetSort | Unset): Sort by column and direction.
        filter_ (Filter | None | Unset): Filter tree.
    """

    limit: int | None | Unset = 1000
    page: int | None | Unset = 1
    sort: None | SheetSort | Unset = UNSET
    filter_: Filter | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.filter_ import Filter
        from ..models.sheet_sort import SheetSort

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

        sort: dict[str, Any] | None | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        elif isinstance(self.sort, SheetSort):
            sort = self.sort.to_dict()
        else:
            sort = self.sort

        filter_: dict[str, Any] | None | Unset
        if isinstance(self.filter_, Unset):
            filter_ = UNSET
        elif isinstance(self.filter_, Filter):
            filter_ = self.filter_.to_dict()
        else:
            filter_ = self.filter_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limit is not UNSET:
            field_dict["limit"] = limit
        if page is not UNSET:
            field_dict["page"] = page
        if sort is not UNSET:
            field_dict["sort"] = sort
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_ import Filter
        from ..models.sheet_sort import SheetSort

        d = dict(src_dict)

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

        def _parse_sort(data: object) -> None | SheetSort | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sort_type_1 = SheetSort.from_dict(data)

                return sort_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SheetSort | Unset, data)

        sort = _parse_sort(d.pop("sort", UNSET))

        def _parse_filter_(data: object) -> Filter | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filter_type_1 = Filter.from_dict(data)

                return filter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Filter | None | Unset, data)

        filter_ = _parse_filter_(d.pop("filter", UNSET))

        sheet_data_request = cls(
            limit=limit,
            page=page,
            sort=sort,
            filter_=filter_,
        )

        sheet_data_request.additional_properties = d
        return sheet_data_request

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
