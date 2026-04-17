from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.view_query_request import ViewQueryRequest


T = TypeVar("T", bound="UpdateSheetRequest")


@_attrs_define
class UpdateSheetRequest:
    """
    Attributes:
        name (str): Display name
        description (str):
        view_definition (None | Unset | ViewQueryRequest): Updated view definition (VIEW sheets only)
    """

    name: str
    description: str
    view_definition: None | Unset | ViewQueryRequest = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.view_query_request import ViewQueryRequest

        name = self.name

        description = self.description

        view_definition: dict[str, Any] | None | Unset
        if isinstance(self.view_definition, Unset):
            view_definition = UNSET
        elif isinstance(self.view_definition, ViewQueryRequest):
            view_definition = self.view_definition.to_dict()
        else:
            view_definition = self.view_definition

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
            }
        )
        if view_definition is not UNSET:
            field_dict["viewDefinition"] = view_definition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.view_query_request import ViewQueryRequest

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        def _parse_view_definition(data: object) -> None | Unset | ViewQueryRequest:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                view_definition_type_1 = ViewQueryRequest.from_dict(data)

                return view_definition_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViewQueryRequest, data)

        view_definition = _parse_view_definition(d.pop("viewDefinition", UNSET))

        update_sheet_request = cls(
            name=name,
            description=description,
            view_definition=view_definition,
        )

        update_sheet_request.additional_properties = d
        return update_sheet_request

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
