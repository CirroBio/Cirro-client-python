from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LoginProvider")


@_attrs_define
class LoginProvider:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        logo_url (str):
    """

    id: str
    name: str
    description: str
    logo_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        logo_url = self.logo_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "logoUrl": logo_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        logo_url = d.pop("logoUrl")

        login_provider = cls(
            id=id,
            name=name,
            description=description,
            logo_url=logo_url,
        )

        login_provider.additional_properties = d
        return login_provider

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
