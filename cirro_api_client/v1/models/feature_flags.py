from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FeatureFlags")


@_attrs_define
class FeatureFlags:
    """
    Attributes:
        sftp_enabled (bool):
        governance_enabled (bool):
        project_requests_enabled (bool):
        workspaces_enabled (bool):
        drive_enabled (bool):
        app_registrations_enabled (bool):
        machine_auth_enabled (bool):
        sheets_enabled (bool):
        ai_enabled (bool):
        shared_filesystems_enabled (bool):
        custom_workspace_roles_enabled (bool):
        orcid_integration_enabled (bool):
    """

    sftp_enabled: bool
    governance_enabled: bool
    project_requests_enabled: bool
    workspaces_enabled: bool
    drive_enabled: bool
    app_registrations_enabled: bool
    machine_auth_enabled: bool
    sheets_enabled: bool
    ai_enabled: bool
    shared_filesystems_enabled: bool
    custom_workspace_roles_enabled: bool
    orcid_integration_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sftp_enabled = self.sftp_enabled

        governance_enabled = self.governance_enabled

        project_requests_enabled = self.project_requests_enabled

        workspaces_enabled = self.workspaces_enabled

        drive_enabled = self.drive_enabled

        app_registrations_enabled = self.app_registrations_enabled

        machine_auth_enabled = self.machine_auth_enabled

        sheets_enabled = self.sheets_enabled

        ai_enabled = self.ai_enabled

        shared_filesystems_enabled = self.shared_filesystems_enabled

        custom_workspace_roles_enabled = self.custom_workspace_roles_enabled

        orcid_integration_enabled = self.orcid_integration_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sftpEnabled": sftp_enabled,
                "governanceEnabled": governance_enabled,
                "projectRequestsEnabled": project_requests_enabled,
                "workspacesEnabled": workspaces_enabled,
                "driveEnabled": drive_enabled,
                "appRegistrationsEnabled": app_registrations_enabled,
                "machineAuthEnabled": machine_auth_enabled,
                "sheetsEnabled": sheets_enabled,
                "aiEnabled": ai_enabled,
                "sharedFilesystemsEnabled": shared_filesystems_enabled,
                "customWorkspaceRolesEnabled": custom_workspace_roles_enabled,
                "orcidIntegrationEnabled": orcid_integration_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sftp_enabled = d.pop("sftpEnabled")

        governance_enabled = d.pop("governanceEnabled")

        project_requests_enabled = d.pop("projectRequestsEnabled")

        workspaces_enabled = d.pop("workspacesEnabled")

        drive_enabled = d.pop("driveEnabled")

        app_registrations_enabled = d.pop("appRegistrationsEnabled")

        machine_auth_enabled = d.pop("machineAuthEnabled")

        sheets_enabled = d.pop("sheetsEnabled")

        ai_enabled = d.pop("aiEnabled")

        shared_filesystems_enabled = d.pop("sharedFilesystemsEnabled")

        custom_workspace_roles_enabled = d.pop("customWorkspaceRolesEnabled")

        orcid_integration_enabled = d.pop("orcidIntegrationEnabled")

        feature_flags = cls(
            sftp_enabled=sftp_enabled,
            governance_enabled=governance_enabled,
            project_requests_enabled=project_requests_enabled,
            workspaces_enabled=workspaces_enabled,
            drive_enabled=drive_enabled,
            app_registrations_enabled=app_registrations_enabled,
            machine_auth_enabled=machine_auth_enabled,
            sheets_enabled=sheets_enabled,
            ai_enabled=ai_enabled,
            shared_filesystems_enabled=shared_filesystems_enabled,
            custom_workspace_roles_enabled=custom_workspace_roles_enabled,
            orcid_integration_enabled=orcid_integration_enabled,
        )

        feature_flags.additional_properties = d
        return feature_flags

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
