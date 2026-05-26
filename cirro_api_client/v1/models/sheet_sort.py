from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sql_sort_order import SqlSortOrder
from ..types import UNSET, Unset

T = TypeVar("T", bound="SheetSort")


@_attrs_define
class SheetSort:
    """Column and direction for sorting sheet data results.

    Attributes:
        order_by (None | str | Unset): Column to sort by.
        order (None | SqlSortOrder | Unset): Sort direction. Default: SqlSortOrder.ASC.
    """

    order_by: None | str | Unset = UNSET
    order: None | SqlSortOrder | Unset = SqlSortOrder.ASC
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_by: None | str | Unset
        if isinstance(self.order_by, Unset):
            order_by = UNSET
        else:
            order_by = self.order_by

        order: None | str | Unset
        if isinstance(self.order, Unset):
            order = UNSET
        elif isinstance(self.order, SqlSortOrder):
            order = self.order.value
        else:
            order = self.order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_by is not UNSET:
            field_dict["orderBy"] = order_by
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_order_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        order_by = _parse_order_by(d.pop("orderBy", UNSET))

        def _parse_order(data: object) -> None | SqlSortOrder | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_type_1 = SqlSortOrder(data)

                return order_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SqlSortOrder | Unset, data)

        order = _parse_order(d.pop("order", UNSET))

        sheet_sort = cls(
            order_by=order_by,
            order=order,
        )

        sheet_sort.additional_properties = d
        return sheet_sort

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
