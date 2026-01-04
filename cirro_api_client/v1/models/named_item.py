from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NamedItem")


@_attrs_define
class NamedItem:
    """
    Attributes:
        id (str):
        name (str):
    """

    id: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        named_item = cls(
            id=id,
            name=name,
        )

        named_item.additional_properties = d
        return named_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
