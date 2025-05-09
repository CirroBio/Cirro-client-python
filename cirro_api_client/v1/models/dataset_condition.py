from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_condition_field import DatasetConditionField

T = TypeVar("T", bound="DatasetCondition")


@_attrs_define
class DatasetCondition:
    """
    Attributes:
        field (DatasetConditionField):
        value (str):
    """

    field: DatasetConditionField
    value: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field = self.field.value

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field = DatasetConditionField(d.pop("field"))

        value = d.pop("value")

        dataset_condition = cls(
            field=field,
            value=value,
        )

        dataset_condition.additional_properties = d
        return dataset_condition

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())
