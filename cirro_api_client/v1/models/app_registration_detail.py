from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.app_client_type import AppClientType
from ..models.app_type import AppType
from ..models.permission import Permission
from ..models.principal_type import PrincipalType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_permission_set import ProjectPermissionSet


T = TypeVar("T", bound="AppRegistrationDetail")


@_attrs_define
class AppRegistrationDetail:
    """
    Attributes:
        id (str):
        client_id (str):
        name (str):
        description (str):
        principal_type (PrincipalType):
        type_ (AppType):
        client_type (AppClientType):
        project_permissions (list[ProjectPermissionSet]):
        global_permissions (list[Permission]):
        is_archived (bool):
        requires_admin_consent (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        created_by (str):
        allowed_ips (list[str] | None | Unset):
        redirect_uris (list[str] | None | Unset):
        secret_expires_at (datetime.datetime | None | Unset):
        secret_generated_at (datetime.datetime | None | Unset):
        secret_generated_by (None | str | Unset):
        approved_at (datetime.datetime | None | Unset):
        approved_by (None | str | Unset):
    """

    id: str
    client_id: str
    name: str
    description: str
    principal_type: PrincipalType
    type_: AppType
    client_type: AppClientType
    project_permissions: list[ProjectPermissionSet]
    global_permissions: list[Permission]
    is_archived: bool
    requires_admin_consent: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    created_by: str
    allowed_ips: list[str] | None | Unset = UNSET
    redirect_uris: list[str] | None | Unset = UNSET
    secret_expires_at: datetime.datetime | None | Unset = UNSET
    secret_generated_at: datetime.datetime | None | Unset = UNSET
    secret_generated_by: None | str | Unset = UNSET
    approved_at: datetime.datetime | None | Unset = UNSET
    approved_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        client_id = self.client_id

        name = self.name

        description = self.description

        principal_type = self.principal_type.value

        type_ = self.type_.value

        client_type = self.client_type.value

        project_permissions = []
        for project_permissions_item_data in self.project_permissions:
            project_permissions_item = project_permissions_item_data.to_dict()
            project_permissions.append(project_permissions_item)

        global_permissions = []
        for global_permissions_item_data in self.global_permissions:
            global_permissions_item = global_permissions_item_data.value
            global_permissions.append(global_permissions_item)

        is_archived = self.is_archived

        requires_admin_consent = self.requires_admin_consent

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        created_by = self.created_by

        allowed_ips: list[str] | None | Unset
        if isinstance(self.allowed_ips, Unset):
            allowed_ips = UNSET
        elif isinstance(self.allowed_ips, list):
            allowed_ips = self.allowed_ips

        else:
            allowed_ips = self.allowed_ips

        redirect_uris: list[str] | None | Unset
        if isinstance(self.redirect_uris, Unset):
            redirect_uris = UNSET
        elif isinstance(self.redirect_uris, list):
            redirect_uris = self.redirect_uris

        else:
            redirect_uris = self.redirect_uris

        secret_expires_at: None | str | Unset
        if isinstance(self.secret_expires_at, Unset):
            secret_expires_at = UNSET
        elif isinstance(self.secret_expires_at, datetime.datetime):
            secret_expires_at = self.secret_expires_at.isoformat()
        else:
            secret_expires_at = self.secret_expires_at

        secret_generated_at: None | str | Unset
        if isinstance(self.secret_generated_at, Unset):
            secret_generated_at = UNSET
        elif isinstance(self.secret_generated_at, datetime.datetime):
            secret_generated_at = self.secret_generated_at.isoformat()
        else:
            secret_generated_at = self.secret_generated_at

        secret_generated_by: None | str | Unset
        if isinstance(self.secret_generated_by, Unset):
            secret_generated_by = UNSET
        else:
            secret_generated_by = self.secret_generated_by

        approved_at: None | str | Unset
        if isinstance(self.approved_at, Unset):
            approved_at = UNSET
        elif isinstance(self.approved_at, datetime.datetime):
            approved_at = self.approved_at.isoformat()
        else:
            approved_at = self.approved_at

        approved_by: None | str | Unset
        if isinstance(self.approved_by, Unset):
            approved_by = UNSET
        else:
            approved_by = self.approved_by

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
                "projectPermissions": project_permissions,
                "globalPermissions": global_permissions,
                "isArchived": is_archived,
                "requiresAdminConsent": requires_admin_consent,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "createdBy": created_by,
            }
        )
        if allowed_ips is not UNSET:
            field_dict["allowedIps"] = allowed_ips
        if redirect_uris is not UNSET:
            field_dict["redirectUris"] = redirect_uris
        if secret_expires_at is not UNSET:
            field_dict["secretExpiresAt"] = secret_expires_at
        if secret_generated_at is not UNSET:
            field_dict["secretGeneratedAt"] = secret_generated_at
        if secret_generated_by is not UNSET:
            field_dict["secretGeneratedBy"] = secret_generated_by
        if approved_at is not UNSET:
            field_dict["approvedAt"] = approved_at
        if approved_by is not UNSET:
            field_dict["approvedBy"] = approved_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_permission_set import ProjectPermissionSet

        d = dict(src_dict)
        id = d.pop("id")

        client_id = d.pop("clientId")

        name = d.pop("name")

        description = d.pop("description")

        principal_type = PrincipalType(d.pop("principalType"))

        type_ = AppType(d.pop("type"))

        client_type = AppClientType(d.pop("clientType"))

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

        is_archived = d.pop("isArchived")

        requires_admin_consent = d.pop("requiresAdminConsent")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        created_by = d.pop("createdBy")

        def _parse_allowed_ips(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_ips_type_0 = cast(list[str], data)

                return allowed_ips_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_ips = _parse_allowed_ips(d.pop("allowedIps", UNSET))

        def _parse_redirect_uris(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                redirect_uris_type_0 = cast(list[str], data)

                return redirect_uris_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        redirect_uris = _parse_redirect_uris(d.pop("redirectUris", UNSET))

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

        def _parse_secret_generated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                secret_generated_at_type_0 = isoparse(data)

                return secret_generated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        secret_generated_at = _parse_secret_generated_at(d.pop("secretGeneratedAt", UNSET))

        def _parse_secret_generated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secret_generated_by = _parse_secret_generated_by(d.pop("secretGeneratedBy", UNSET))

        def _parse_approved_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_at_type_0 = isoparse(data)

                return approved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        approved_at = _parse_approved_at(d.pop("approvedAt", UNSET))

        def _parse_approved_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approved_by = _parse_approved_by(d.pop("approvedBy", UNSET))

        app_registration_detail = cls(
            id=id,
            client_id=client_id,
            name=name,
            description=description,
            principal_type=principal_type,
            type_=type_,
            client_type=client_type,
            project_permissions=project_permissions,
            global_permissions=global_permissions,
            is_archived=is_archived,
            requires_admin_consent=requires_admin_consent,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            allowed_ips=allowed_ips,
            redirect_uris=redirect_uris,
            secret_expires_at=secret_expires_at,
            secret_generated_at=secret_generated_at,
            secret_generated_by=secret_generated_by,
            approved_at=approved_at,
            approved_by=approved_by,
        )

        app_registration_detail.additional_properties = d
        return app_registration_detail

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
