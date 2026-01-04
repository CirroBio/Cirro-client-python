from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostponeWorkspaceAutostopInput")


@_attrs_define
class PostponeWorkspaceAutostopInput:
    """
    Attributes:
        auto_stop_timeout (Union[Unset, int]): Time period (in hours) to automatically stop the workspace if running
    """

    auto_stop_timeout: Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_stop_timeout = self.auto_stop_timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_stop_timeout is not UNSET:
            field_dict["autoStopTimeout"] = auto_stop_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        auto_stop_timeout = d.pop("autoStopTimeout", UNSET)

        postpone_workspace_autostop_input = cls(
            auto_stop_timeout=auto_stop_timeout,
        )

        postpone_workspace_autostop_input.additional_properties = d
        return postpone_workspace_autostop_input

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
