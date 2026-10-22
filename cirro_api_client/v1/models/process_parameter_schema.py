from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_parameter_schema_form import ProcessParameterSchemaForm
    from ..models.process_parameter_schema_structured_inputs import ProcessParameterSchemaStructuredInputs
    from ..models.process_parameter_schema_ui import ProcessParameterSchemaUi


T = TypeVar("T", bound="ProcessParameterSchema")


@_attrs_define
class ProcessParameterSchema:
    """
    Attributes:
        form (ProcessParameterSchemaForm | Unset): JSONSchema representation of the form rendered for the end-user when
            executing a pipeline
        ui (ProcessParameterSchemaUi | Unset): Describes how the form should be rendered on the UI, see rjsf uiSchema
            customizations
        structured_inputs (ProcessParameterSchemaStructuredInputs | Unset): Structured file inputs required by this
            process, keyed by requirement name (referenced elsewhere, e.g. in form, by this same key)
    """

    form: ProcessParameterSchemaForm | Unset = UNSET
    ui: ProcessParameterSchemaUi | Unset = UNSET
    structured_inputs: ProcessParameterSchemaStructuredInputs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        form: dict[str, Any] | Unset = UNSET
        if not isinstance(self.form, Unset):
            form = self.form.to_dict()

        ui: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ui, Unset):
            ui = self.ui.to_dict()

        structured_inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.structured_inputs, Unset):
            structured_inputs = self.structured_inputs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if form is not UNSET:
            field_dict["form"] = form
        if ui is not UNSET:
            field_dict["ui"] = ui
        if structured_inputs is not UNSET:
            field_dict["structuredInputs"] = structured_inputs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_parameter_schema_form import ProcessParameterSchemaForm
        from ..models.process_parameter_schema_structured_inputs import ProcessParameterSchemaStructuredInputs
        from ..models.process_parameter_schema_ui import ProcessParameterSchemaUi

        d = dict(src_dict)
        _form = d.pop("form", UNSET)
        form: ProcessParameterSchemaForm | Unset
        if isinstance(_form, Unset):
            form = UNSET
        else:
            form = ProcessParameterSchemaForm.from_dict(_form)

        _ui = d.pop("ui", UNSET)
        ui: ProcessParameterSchemaUi | Unset
        if isinstance(_ui, Unset):
            ui = UNSET
        else:
            ui = ProcessParameterSchemaUi.from_dict(_ui)

        _structured_inputs = d.pop("structuredInputs", UNSET)
        structured_inputs: ProcessParameterSchemaStructuredInputs | Unset
        if isinstance(_structured_inputs, Unset):
            structured_inputs = UNSET
        else:
            structured_inputs = ProcessParameterSchemaStructuredInputs.from_dict(_structured_inputs)

        process_parameter_schema = cls(
            form=form,
            ui=ui,
            structured_inputs=structured_inputs,
        )

        process_parameter_schema.additional_properties = d
        return process_parameter_schema

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
