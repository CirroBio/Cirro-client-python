from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ComputeEnvironmentConfigurationProperties")


@_attrs_define
class ComputeEnvironmentConfigurationProperties:
    """Configuration properties passed to the environment"""

    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        compute_environment_configuration_properties = cls()

        compute_environment_configuration_properties.additional_properties = d
        return compute_environment_configuration_properties

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
