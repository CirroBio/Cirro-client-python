from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_format import FileFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.input_file_requirement_examples import InputFileRequirementExamples
    from ..models.input_file_requirement_schema import InputFileRequirementSchema


T = TypeVar("T", bound="InputFileRequirement")


@_attrs_define
class InputFileRequirement:
    """Defines a structured file that a pipeline accepts as an input, and the schema used to validate it

    Attributes:
        file_format (FileFormat): Determines the file format used when passing the schema-validated input to the
            pipeline.
             - CSV: comma-delimited, one row per object, header row taken from the schema's property order.
               Nested objects/arrays within a row are JSON-encoded inline as a single cell value (not recommended).
             - TSV: same as CSV, but tab-delimited.
             - JSON: the row objects are written out unmodified as a JSON array (no flattening).
        schema (InputFileRequirementSchema): JSONSchema representation of the input file contents
        examples (list[InputFileRequirementExamples] | None | Unset): Example rows of data conforming to the schema,
            shown to the user as a starting point
    """

    file_format: FileFormat
    schema: InputFileRequirementSchema
    examples: list[InputFileRequirementExamples] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_format = self.file_format.value

        schema = self.schema.to_dict()

        examples: list[dict[str, Any]] | None | Unset
        if isinstance(self.examples, Unset):
            examples = UNSET
        elif isinstance(self.examples, list):
            examples = []
            for examples_type_0_item_data in self.examples:
                examples_type_0_item = examples_type_0_item_data.to_dict()
                examples.append(examples_type_0_item)

        else:
            examples = self.examples

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileFormat": file_format,
                "schema": schema,
            }
        )
        if examples is not UNSET:
            field_dict["examples"] = examples

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_file_requirement_examples import InputFileRequirementExamples
        from ..models.input_file_requirement_schema import InputFileRequirementSchema

        d = dict(src_dict)
        file_format = FileFormat(d.pop("fileFormat"))

        schema = InputFileRequirementSchema.from_dict(d.pop("schema"))

        def _parse_examples(data: object) -> list[InputFileRequirementExamples] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                examples_type_0 = []
                _examples_type_0 = data
                for examples_type_0_item_data in _examples_type_0:
                    examples_type_0_item = InputFileRequirementExamples.from_dict(examples_type_0_item_data)

                    examples_type_0.append(examples_type_0_item)

                return examples_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InputFileRequirementExamples] | None | Unset, data)

        examples = _parse_examples(d.pop("examples", UNSET))

        input_file_requirement = cls(
            file_format=file_format,
            schema=schema,
            examples=examples,
        )

        input_file_requirement.additional_properties = d
        return input_file_requirement

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
