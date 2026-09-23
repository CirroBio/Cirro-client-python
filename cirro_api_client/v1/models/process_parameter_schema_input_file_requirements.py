from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.input_file_requirement import InputFileRequirement


T = TypeVar("T", bound="ProcessParameterSchemaInputFileRequirements")


@_attrs_define
class ProcessParameterSchemaInputFileRequirements:
    """Structured file inputs required by this process, keyed by requirement name (referenced elsewhere, e.g. in form, by
    this same key)

    """

    additional_properties: dict[str, InputFileRequirement] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_file_requirement import InputFileRequirement

        d = dict(src_dict)
        process_parameter_schema_input_file_requirements = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = InputFileRequirement.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        process_parameter_schema_input_file_requirements.additional_properties = additional_properties
        return process_parameter_schema_input_file_requirements

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> InputFileRequirement:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: InputFileRequirement) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
