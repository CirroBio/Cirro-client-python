from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Contact")


@_attrs_define
class Contact:
    """
    Attributes:
        name (str):
        organization (str):
        email (str):
        phone (str):
    """

    name: str
    organization: str
    email: str
    phone: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        organization = self.organization

        email = self.email

        phone = self.phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "organization": organization,
                "email": email,
                "phone": phone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        organization = d.pop("organization")

        email = d.pop("email")

        phone = d.pop("phone")

        contact = cls(
            name=name,
            organization=organization,
            email=email,
            phone=phone,
        )

        contact.additional_properties = d
        return contact

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
