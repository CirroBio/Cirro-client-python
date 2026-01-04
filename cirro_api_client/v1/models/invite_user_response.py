from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InviteUserResponse")


@_attrs_define
class InviteUserResponse:
    """
    Attributes:
        message (str):
    """

    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message")

        invite_user_response = cls(
            message=message,
        )

        invite_user_response.additional_properties = d
        return invite_user_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
