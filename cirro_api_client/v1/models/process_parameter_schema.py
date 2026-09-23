from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_parameter_schema_form import ProcessParameterSchemaForm
    from ..models.process_parameter_schema_input_file_requirements import ProcessParameterSchemaInputFileRequirements
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
        input_file_requirements (ProcessParameterSchemaInputFileRequirements | Unset): Structured file inputs required
            by this process, keyed by requirement name (referenced elsewhere, e.g. in form, by this same key)
    """

    form: ProcessParameterSchemaForm | Unset = UNSET
    ui: ProcessParameterSchemaUi | Unset = UNSET
    input_file_requirements: ProcessParameterSchemaInputFileRequirements | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        form: dict[str, Any] | Unset = UNSET
        if not isinstance(self.form, Unset):
            form = self.form.to_dict()

        ui: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ui, Unset):
            ui = self.ui.to_dict()

        input_file_requirements: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_file_requirements, Unset):
            input_file_requirements = self.input_file_requirements.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if form is not UNSET:
            field_dict["form"] = form
        if ui is not UNSET:
            field_dict["ui"] = ui
        if input_file_requirements is not UNSET:
            field_dict["inputFileRequirements"] = input_file_requirements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_parameter_schema_form import ProcessParameterSchemaForm
        from ..models.process_parameter_schema_input_file_requirements import (
            ProcessParameterSchemaInputFileRequirements,
        )
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

        _input_file_requirements = d.pop("inputFileRequirements", UNSET)
        input_file_requirements: ProcessParameterSchemaInputFileRequirements | Unset
        if isinstance(_input_file_requirements, Unset):
            input_file_requirements = UNSET
        else:
            input_file_requirements = ProcessParameterSchemaInputFileRequirements.from_dict(_input_file_requirements)

        process_parameter_schema = cls(
            form=form,
            ui=ui,
            input_file_requirements=input_file_requirements,
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
