from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.join_type import JoinType

if TYPE_CHECKING:
    from ..models.join_condition import JoinCondition


T = TypeVar("T", bound="ViewJoin")


@_attrs_define
class ViewJoin:
    """
    Attributes:
        sheet_alias (str): Alias of the sheet to join
        join_type (JoinType):
        conditions (list[JoinCondition]):
    """

    sheet_alias: str
    join_type: JoinType
    conditions: list[JoinCondition]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sheet_alias = self.sheet_alias

        join_type = self.join_type.value

        conditions = []
        for conditions_item_data in self.conditions:
            conditions_item = conditions_item_data.to_dict()
            conditions.append(conditions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sheetAlias": sheet_alias,
                "joinType": join_type,
                "conditions": conditions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.join_condition import JoinCondition

        d = dict(src_dict)
        sheet_alias = d.pop("sheetAlias")

        join_type = JoinType(d.pop("joinType"))

        conditions = []
        _conditions = d.pop("conditions")
        for conditions_item_data in _conditions:
            conditions_item = JoinCondition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        view_join = cls(
            sheet_alias=sheet_alias,
            join_type=join_type,
            conditions=conditions,
        )

        view_join.additional_properties = d
        return view_join

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
