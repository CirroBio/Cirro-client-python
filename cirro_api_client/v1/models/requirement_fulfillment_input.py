import datetime
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequirementFulfillmentInput")


@_attrs_define
class RequirementFulfillmentInput:
    """
    Attributes:
        file (Union[None, Unset, str]):
        completed_on (Union[None, Unset, datetime.datetime]): If not provided, defaults to the current instant
    """

    file: None | Unset | str = UNSET
    completed_on: None | Unset | datetime.datetime = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file: None | Unset | str
        if isinstance(self.file, Unset):
            file = UNSET
        else:
            file = self.file

        completed_on: None | Unset | str
        if isinstance(self.completed_on, Unset):
            completed_on = UNSET
        elif isinstance(self.completed_on, datetime.datetime):
            completed_on = self.completed_on.isoformat()
        else:
            completed_on = self.completed_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file
        if completed_on is not UNSET:
            field_dict["completedOn"] = completed_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_file(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        file = _parse_file(d.pop("file", UNSET))

        def _parse_completed_on(data: object) -> None | Unset | datetime.datetime:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_on_type_0 = isoparse(data)

                return completed_on_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.datetime, data)

        completed_on = _parse_completed_on(d.pop("completedOn", UNSET))

        requirement_fulfillment_input = cls(
            file=file,
            completed_on=completed_on,
        )

        requirement_fulfillment_input.additional_properties = d
        return requirement_fulfillment_input

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
