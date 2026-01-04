from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_role import ProjectRole

T = TypeVar("T", bound="ApproveProjectAccessRequest")


@_attrs_define
class ApproveProjectAccessRequest:
    """
    Attributes:
        role (ProjectRole):
    """

    role: ProjectRole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        role = ProjectRole(d.pop("role"))

        approve_project_access_request = cls(
            role=role,
        )

        approve_project_access_request.additional_properties = d
        return approve_project_access_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
