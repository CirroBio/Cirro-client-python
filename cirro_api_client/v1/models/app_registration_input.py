from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.app_client_type import AppClientType
from ..models.permission import Permission
from ..models.principal_type import PrincipalType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_permission_set import ProjectPermissionSet


T = TypeVar("T", bound="AppRegistrationInput")


@_attrs_define
class AppRegistrationInput:
    """
    Attributes:
        name (str): Name of app registration
        description (str):
        principal_type (PrincipalType):
        client_type (AppClientType):
        allowed_ips (list[str]): These IP address ranges are allowed to use this app (will be used later)
        redirect_uris (list[str]): A list of allowed redirect URIs for authentication. HTTPS is required except for
            localhost and app callback URLs are supported
        project_permissions (list[ProjectPermissionSet]): Permissions that this app has on the project
        global_permissions (list[Permission]): Permissions that this app has globally
        logo_url (None | str | Unset): Set a logo for the app, only available for administrators
        app_url (None | str | Unset): Set a link for more information on the app
        publisher (None | str | Unset): Set a publisher display name, only available for administrators
        secret_expires_at (datetime.datetime | None | Unset): Optional expiry date of secret
        discovery_enabled (bool | None | Unset): Enables dynamic client registration to discover this app (useful for
            MCPs), only available for administrators
        template_id (None | str | Unset): ID of the app registration template
    """

    name: str
    description: str
    principal_type: PrincipalType
    client_type: AppClientType
    allowed_ips: list[str]
    redirect_uris: list[str]
    project_permissions: list[ProjectPermissionSet]
    global_permissions: list[Permission]
    logo_url: None | str | Unset = UNSET
    app_url: None | str | Unset = UNSET
    publisher: None | str | Unset = UNSET
    secret_expires_at: datetime.datetime | None | Unset = UNSET
    discovery_enabled: bool | None | Unset = UNSET
    template_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        principal_type = self.principal_type.value

        client_type = self.client_type.value

        allowed_ips = self.allowed_ips

        redirect_uris = self.redirect_uris

        project_permissions = []
        for project_permissions_item_data in self.project_permissions:
            project_permissions_item = project_permissions_item_data.to_dict()
            project_permissions.append(project_permissions_item)

        global_permissions = []
        for global_permissions_item_data in self.global_permissions:
            global_permissions_item = global_permissions_item_data.value
            global_permissions.append(global_permissions_item)

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        app_url: None | str | Unset
        if isinstance(self.app_url, Unset):
            app_url = UNSET
        else:
            app_url = self.app_url

        publisher: None | str | Unset
        if isinstance(self.publisher, Unset):
            publisher = UNSET
        else:
            publisher = self.publisher

        secret_expires_at: None | str | Unset
        if isinstance(self.secret_expires_at, Unset):
            secret_expires_at = UNSET
        elif isinstance(self.secret_expires_at, datetime.datetime):
            secret_expires_at = self.secret_expires_at.isoformat()
        else:
            secret_expires_at = self.secret_expires_at

        discovery_enabled: bool | None | Unset
        if isinstance(self.discovery_enabled, Unset):
            discovery_enabled = UNSET
        else:
            discovery_enabled = self.discovery_enabled

        template_id: None | str | Unset
        if isinstance(self.template_id, Unset):
            template_id = UNSET
        else:
            template_id = self.template_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "principalType": principal_type,
                "clientType": client_type,
                "allowedIps": allowed_ips,
                "redirectUris": redirect_uris,
                "projectPermissions": project_permissions,
                "globalPermissions": global_permissions,
            }
        )
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if app_url is not UNSET:
            field_dict["appUrl"] = app_url
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if secret_expires_at is not UNSET:
            field_dict["secretExpiresAt"] = secret_expires_at
        if discovery_enabled is not UNSET:
            field_dict["discoveryEnabled"] = discovery_enabled
        if template_id is not UNSET:
            field_dict["templateId"] = template_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_permission_set import ProjectPermissionSet

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        principal_type = PrincipalType(d.pop("principalType"))

        client_type = AppClientType(d.pop("clientType"))

        allowed_ips = cast(list[str], d.pop("allowedIps"))

        redirect_uris = cast(list[str], d.pop("redirectUris"))

        project_permissions = []
        _project_permissions = d.pop("projectPermissions")
        for project_permissions_item_data in _project_permissions:
            project_permissions_item = ProjectPermissionSet.from_dict(project_permissions_item_data)

            project_permissions.append(project_permissions_item)

        global_permissions = []
        _global_permissions = d.pop("globalPermissions")
        for global_permissions_item_data in _global_permissions:
            global_permissions_item = Permission(global_permissions_item_data)

            global_permissions.append(global_permissions_item)

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logoUrl", UNSET))

        def _parse_app_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_url = _parse_app_url(d.pop("appUrl", UNSET))

        def _parse_publisher(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publisher = _parse_publisher(d.pop("publisher", UNSET))

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

        def _parse_discovery_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        discovery_enabled = _parse_discovery_enabled(d.pop("discoveryEnabled", UNSET))

        def _parse_template_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_id = _parse_template_id(d.pop("templateId", UNSET))

        app_registration_input = cls(
            name=name,
            description=description,
            principal_type=principal_type,
            client_type=client_type,
            allowed_ips=allowed_ips,
            redirect_uris=redirect_uris,
            project_permissions=project_permissions,
            global_permissions=global_permissions,
            logo_url=logo_url,
            app_url=app_url,
            publisher=publisher,
            secret_expires_at=secret_expires_at,
            discovery_enabled=discovery_enabled,
            template_id=template_id,
        )

        app_registration_input.additional_properties = d
        return app_registration_input

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
