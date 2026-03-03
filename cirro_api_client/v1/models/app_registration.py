from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.app_client_type import AppClientType
from ..models.app_type import AppType
from ..models.principal_type import PrincipalType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppRegistration")


@_attrs_define
class AppRegistration:
    """
    Attributes:
        id (str):
        client_id (str):
        name (str):
        description (str):
        principal_type (PrincipalType):
        type_ (AppType):
        client_type (AppClientType):
        is_archived (bool):
        requires_admin_consent (bool):
        updated_at (datetime.datetime):
        created_at (datetime.datetime):
        created_by (str):
        secret_expires_at (datetime.datetime | None | Unset):
    """

    id: str
    client_id: str
    name: str
    description: str
    principal_type: PrincipalType
    type_: AppType
    client_type: AppClientType
    is_archived: bool
    requires_admin_consent: bool
    updated_at: datetime.datetime
    created_at: datetime.datetime
    created_by: str
    secret_expires_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        client_id = self.client_id

        name = self.name

        description = self.description

        principal_type = self.principal_type.value

        type_ = self.type_.value

        client_type = self.client_type.value

        is_archived = self.is_archived

        requires_admin_consent = self.requires_admin_consent

        updated_at = self.updated_at.isoformat()

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        secret_expires_at: None | str | Unset
        if isinstance(self.secret_expires_at, Unset):
            secret_expires_at = UNSET
        elif isinstance(self.secret_expires_at, datetime.datetime):
            secret_expires_at = self.secret_expires_at.isoformat()
        else:
            secret_expires_at = self.secret_expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "clientId": client_id,
                "name": name,
                "description": description,
                "principalType": principal_type,
                "type": type_,
                "clientType": client_type,
                "isArchived": is_archived,
                "requiresAdminConsent": requires_admin_consent,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "createdBy": created_by,
            }
        )
        if secret_expires_at is not UNSET:
            field_dict["secretExpiresAt"] = secret_expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        client_id = d.pop("clientId")

        name = d.pop("name")

        description = d.pop("description")

        principal_type = PrincipalType(d.pop("principalType"))

        type_ = AppType(d.pop("type"))

        client_type = AppClientType(d.pop("clientType"))

        is_archived = d.pop("isArchived")

        requires_admin_consent = d.pop("requiresAdminConsent")

        updated_at = isoparse(d.pop("updatedAt"))

        created_at = isoparse(d.pop("createdAt"))

        created_by = d.pop("createdBy")

        def _parse_secret_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                secret_expires_at_type_0 = isoparse(data)

                return secret_expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        secret_expires_at = _parse_secret_expires_at(d.pop("secretExpiresAt", UNSET))

        app_registration = cls(
            id=id,
            client_id=client_id,
            name=name,
            description=description,
            principal_type=principal_type,
            type_=type_,
            client_type=client_type,
            is_archived=is_archived,
            requires_admin_consent=requires_admin_consent,
            updated_at=updated_at,
            created_at=created_at,
            created_by=created_by,
            secret_expires_at=secret_expires_at,
        )

        app_registration.additional_properties = d
        return app_registration

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
