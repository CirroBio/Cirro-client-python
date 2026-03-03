from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AppRegistrationSecretResponse")


@_attrs_define
class AppRegistrationSecretResponse:
    """
    Attributes:
        id (str):
        client_id (str): The oauth client ID.
        client_secret (str): The oauth client secret. This is only returned once.
        secret_generated_at (datetime.datetime):
    """

    id: str
    client_id: str
    client_secret: str
    secret_generated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        client_id = self.client_id

        client_secret = self.client_secret

        secret_generated_at = self.secret_generated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "clientId": client_id,
                "clientSecret": client_secret,
                "secretGeneratedAt": secret_generated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        client_id = d.pop("clientId")

        client_secret = d.pop("clientSecret")

        secret_generated_at = isoparse(d.pop("secretGeneratedAt"))

        app_registration_secret_response = cls(
            id=id,
            client_id=client_id,
            client_secret=client_secret,
            secret_generated_at=secret_generated_at,
        )

        app_registration_secret_response.additional_properties = d
        return app_registration_secret_response

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
