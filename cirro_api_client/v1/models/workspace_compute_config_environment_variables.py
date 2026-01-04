from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkspaceComputeConfigEnvironmentVariables")


@_attrs_define
class WorkspaceComputeConfigEnvironmentVariables:
    """Map of environment variables injected into the container at runtime. Keys must be non-blank.

    Example:
        {'ENV_MODE': 'production', 'LOG_LEVEL': 'debug'}

    """

    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        workspace_compute_config_environment_variables = cls()

        workspace_compute_config_environment_variables.additional_properties = d
        return workspace_compute_config_environment_variables

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
