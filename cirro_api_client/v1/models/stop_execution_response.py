from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StopExecutionResponse")


@_attrs_define
class StopExecutionResponse:
    """
    Attributes:
        success (Union[Unset, List[str]]): List of job IDs that were successful in termination
        failed (Union[Unset, List[str]]): List of job IDs that were not successful in termination
    """

    success: Unset | list[str] = UNSET
    failed: Unset | list[str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success: Unset | list[str] = UNSET
        if not isinstance(self.success, Unset):
            success = self.success

        failed: Unset | list[str] = UNSET
        if not isinstance(self.failed, Unset):
            failed = self.failed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if failed is not UNSET:
            field_dict["failed"] = failed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        success = cast(list[str], d.pop("success", UNSET))

        failed = cast(list[str], d.pop("failed", UNSET))

        stop_execution_response = cls(
            success=success,
            failed=failed,
        )

        stop_execution_response.additional_properties = d
        return stop_execution_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
