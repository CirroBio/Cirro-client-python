from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_operator import FilterOperator
from ..models.logical_operator import LogicalOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.view_filter_values import ViewFilterValues


T = TypeVar("T", bound="ViewFilter")


@_attrs_define
class ViewFilter:
    """A filter node: either a group (with logicalOperator and conditions) or a leaf condition (with column, operator, and
    values)

        Attributes:
            logical_operator (LogicalOperator | None | Unset): Set for group nodes to combine child conditions
            conditions (list[ViewFilter] | None | Unset): Child filter nodes (for group nodes)
            column (None | str | Unset): Qualified column reference in alias.column format (for leaf nodes) Example: s1.age.
            operator (FilterOperator | None | Unset): Comparison operator (for leaf nodes)
            values (list[ViewFilterValues] | None | Unset): Values for the filter. Single-element list for comparison
                operators (EQUALS, GREATER_THAN, etc.), multi-element for IN/NOT_IN. Null or empty for IS_NULL/IS_NOT_NULL.
    """

    logical_operator: LogicalOperator | None | Unset = UNSET
    conditions: list[ViewFilter] | None | Unset = UNSET
    column: None | str | Unset = UNSET
    operator: FilterOperator | None | Unset = UNSET
    values: list[ViewFilterValues] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logical_operator: None | str | Unset
        if isinstance(self.logical_operator, Unset):
            logical_operator = UNSET
        elif isinstance(self.logical_operator, LogicalOperator):
            logical_operator = self.logical_operator.value
        else:
            logical_operator = self.logical_operator

        conditions: list[dict[str, Any]] | None | Unset
        if isinstance(self.conditions, Unset):
            conditions = UNSET
        elif isinstance(self.conditions, list):
            conditions = []
            for conditions_type_0_item_data in self.conditions:
                conditions_type_0_item = conditions_type_0_item_data.to_dict()
                conditions.append(conditions_type_0_item)

        else:
            conditions = self.conditions

        column: None | str | Unset
        if isinstance(self.column, Unset):
            column = UNSET
        else:
            column = self.column

        operator: None | str | Unset
        if isinstance(self.operator, Unset):
            operator = UNSET
        elif isinstance(self.operator, FilterOperator):
            operator = self.operator.value
        else:
            operator = self.operator

        values: list[dict[str, Any]] | None | Unset
        if isinstance(self.values, Unset):
            values = UNSET
        elif isinstance(self.values, list):
            values = []
            for values_type_0_item_data in self.values:
                values_type_0_item = values_type_0_item_data.to_dict()
                values.append(values_type_0_item)

        else:
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logical_operator is not UNSET:
            field_dict["logicalOperator"] = logical_operator
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if column is not UNSET:
            field_dict["column"] = column
        if operator is not UNSET:
            field_dict["operator"] = operator
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.view_filter_values import ViewFilterValues

        d = dict(src_dict)

        def _parse_logical_operator(data: object) -> LogicalOperator | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                logical_operator_type_1 = LogicalOperator(data)

                return logical_operator_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LogicalOperator | None | Unset, data)

        logical_operator = _parse_logical_operator(d.pop("logicalOperator", UNSET))

        def _parse_conditions(data: object) -> list[ViewFilter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conditions_type_0 = []
                _conditions_type_0 = data
                for conditions_type_0_item_data in _conditions_type_0:
                    conditions_type_0_item = ViewFilter.from_dict(conditions_type_0_item_data)

                    conditions_type_0.append(conditions_type_0_item)

                return conditions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ViewFilter] | None | Unset, data)

        conditions = _parse_conditions(d.pop("conditions", UNSET))

        def _parse_column(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        column = _parse_column(d.pop("column", UNSET))

        def _parse_operator(data: object) -> FilterOperator | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operator_type_1 = FilterOperator(data)

                return operator_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FilterOperator | None | Unset, data)

        operator = _parse_operator(d.pop("operator", UNSET))

        def _parse_values(data: object) -> list[ViewFilterValues] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = []
                _values_type_0 = data
                for values_type_0_item_data in _values_type_0:
                    values_type_0_item = ViewFilterValues.from_dict(values_type_0_item_data)

                    values_type_0.append(values_type_0_item)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ViewFilterValues] | None | Unset, data)

        values = _parse_values(d.pop("values", UNSET))

        view_filter = cls(
            logical_operator=logical_operator,
            conditions=conditions,
            column=column,
            operator=operator,
            values=values,
        )

        view_filter.additional_properties = d
        return view_filter

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
