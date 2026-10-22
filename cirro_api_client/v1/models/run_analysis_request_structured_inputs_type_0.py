from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.structured_input import StructuredInput


T = TypeVar("T", bound="RunAnalysisRequestStructuredInputsType0")


@_attrs_define
class RunAnalysisRequestStructuredInputsType0:
    """Structured file inputs used in the workflow (can be empty), keyed by the input name on the process
    `structuredInputs`

    """

    additional_properties: dict[str, StructuredInput] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.structured_input import StructuredInput

        d = dict(src_dict)
        run_analysis_request_structured_inputs_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = StructuredInput.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        run_analysis_request_structured_inputs_type_0.additional_properties = additional_properties
        return run_analysis_request_structured_inputs_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> StructuredInput:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: StructuredInput) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
