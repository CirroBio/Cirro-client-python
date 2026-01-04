from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.artifact_type import ArtifactType

T = TypeVar("T", bound="Artifact")


@_attrs_define
class Artifact:
    """A secondary file or resource associated with a dataset

    Attributes:
        type (ArtifactType):
        path (str):
    """

    type: ArtifactType
    path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type = self.type.value

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "path": path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ArtifactType(d.pop("type"))

        path = d.pop("path")

        artifact = cls(
            type=type,
            path=path,
        )

        artifact.additional_properties = d
        return artifact

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
