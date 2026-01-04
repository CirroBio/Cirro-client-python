from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ClassificationInput")


@_attrs_define
class ClassificationInput:
    """
    Attributes:
        name (str):
        description (str):
        requirement_ids (List[str]):
    """

    name: str
    description: str
    requirement_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        requirement_ids = self.requirement_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "requirementIds": requirement_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description")

        requirement_ids = cast(list[str], d.pop("requirementIds"))

        classification_input = cls(
            name=name,
            description=description,
            requirement_ids=requirement_ids,
        )

        classification_input.additional_properties = d
        return classification_input

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
