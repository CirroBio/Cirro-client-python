from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgentInputTags")


@_attrs_define
class AgentInputTags:
    """The tags associated with the agent displayed to the user

    Example:
        {'Support Email': 'it@company.com'}

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
        agent_input_tags = cls()

        agent_input_tags.additional_properties = d
        return agent_input_tags

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
