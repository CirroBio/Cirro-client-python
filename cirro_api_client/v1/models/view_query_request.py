from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.view_filter import ViewFilter
    from ..models.view_join import ViewJoin
    from ..models.view_sheet_ref import ViewSheetRef


T = TypeVar("T", bound="ViewQueryRequest")


@_attrs_define
class ViewQueryRequest:
    """Request for a view joining one or more sheets with optional column selection and filtering

    Attributes:
        sheets (list[ViewSheetRef]): Sheets to include in the view
        joins (list[ViewJoin] | None | Unset): Join definitions between sheets
        columns (list[str] | None | Unset): Columns to select in alias.column format. If null, selects all columns.
        filter_ (None | Unset | ViewFilter): Filter conditions to apply
    """

    sheets: list[ViewSheetRef]
    joins: list[ViewJoin] | None | Unset = UNSET
    columns: list[str] | None | Unset = UNSET
    filter_: None | Unset | ViewFilter = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.view_filter import ViewFilter

        sheets = []
        for sheets_item_data in self.sheets:
            sheets_item = sheets_item_data.to_dict()
            sheets.append(sheets_item)

        joins: list[dict[str, Any]] | None | Unset
        if isinstance(self.joins, Unset):
            joins = UNSET
        elif isinstance(self.joins, list):
            joins = []
            for joins_type_0_item_data in self.joins:
                joins_type_0_item = joins_type_0_item_data.to_dict()
                joins.append(joins_type_0_item)

        else:
            joins = self.joins

        columns: list[str] | None | Unset
        if isinstance(self.columns, Unset):
            columns = UNSET
        elif isinstance(self.columns, list):
            columns = self.columns

        else:
            columns = self.columns

        filter_: dict[str, Any] | None | Unset
        if isinstance(self.filter_, Unset):
            filter_ = UNSET
        elif isinstance(self.filter_, ViewFilter):
            filter_ = self.filter_.to_dict()
        else:
            filter_ = self.filter_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sheets": sheets,
            }
        )
        if joins is not UNSET:
            field_dict["joins"] = joins
        if columns is not UNSET:
            field_dict["columns"] = columns
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.view_filter import ViewFilter
        from ..models.view_join import ViewJoin
        from ..models.view_sheet_ref import ViewSheetRef

        d = dict(src_dict)
        sheets = []
        _sheets = d.pop("sheets")
        for sheets_item_data in _sheets:
            sheets_item = ViewSheetRef.from_dict(sheets_item_data)

            sheets.append(sheets_item)

        def _parse_joins(data: object) -> list[ViewJoin] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                joins_type_0 = []
                _joins_type_0 = data
                for joins_type_0_item_data in _joins_type_0:
                    joins_type_0_item = ViewJoin.from_dict(joins_type_0_item_data)

                    joins_type_0.append(joins_type_0_item)

                return joins_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ViewJoin] | None | Unset, data)

        joins = _parse_joins(d.pop("joins", UNSET))

        def _parse_columns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                columns_type_0 = cast(list[str], data)

                return columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        columns = _parse_columns(d.pop("columns", UNSET))

        def _parse_filter_(data: object) -> None | Unset | ViewFilter:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filter_type_1 = ViewFilter.from_dict(data)

                return filter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViewFilter, data)

        filter_ = _parse_filter_(d.pop("filter", UNSET))

        view_query_request = cls(
            sheets=sheets,
            joins=joins,
            columns=columns,
            filter_=filter_,
        )

        view_query_request.additional_properties = d
        return view_query_request

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
