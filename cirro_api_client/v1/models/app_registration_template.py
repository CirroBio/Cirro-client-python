from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_client_type import AppClientType
from ..models.principal_type import PrincipalType

T = TypeVar("T", bound="AppRegistrationTemplate")


@_attrs_define
class AppRegistrationTemplate:
    """
    Attributes:
        id (str):
        name (str):
        publisher (str):
        app_url (str):
        logo_url (str):
        redirect_uris (list[str]):
        principal_type (PrincipalType):
        client_type (AppClientType):
        discovery_enabled (bool):
    """

    id: str
    name: str
    publisher: str
    app_url: str
    logo_url: str
    redirect_uris: list[str]
    principal_type: PrincipalType
    client_type: AppClientType
    discovery_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        publisher = self.publisher

        app_url = self.app_url

        logo_url = self.logo_url

        redirect_uris = self.redirect_uris

        principal_type = self.principal_type.value

        client_type = self.client_type.value

        discovery_enabled = self.discovery_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "publisher": publisher,
                "appUrl": app_url,
                "logoUrl": logo_url,
                "redirectUris": redirect_uris,
                "principalType": principal_type,
                "clientType": client_type,
                "discoveryEnabled": discovery_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        publisher = d.pop("publisher")

        app_url = d.pop("appUrl")

        logo_url = d.pop("logoUrl")

        redirect_uris = cast(list[str], d.pop("redirectUris"))

        principal_type = PrincipalType(d.pop("principalType"))

        client_type = AppClientType(d.pop("clientType"))

        discovery_enabled = d.pop("discoveryEnabled")

        app_registration_template = cls(
            id=id,
            name=name,
            publisher=publisher,
            app_url=app_url,
            logo_url=logo_url,
            redirect_uris=redirect_uris,
            principal_type=principal_type,
            client_type=client_type,
            discovery_enabled=discovery_enabled,
        )

        app_registration_template.additional_properties = d
        return app_registration_template

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
