from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tag")


@_attrs_define
class Tag:
    """
    Attributes:
        value (str): The value of the tag
        editable (Union[Unset, bool]): Whether the tag value is editable Default: True.
        key (Union[None, Unset, str]):
    """

    value: str
    editable: Unset | bool = True
    key: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        editable = self.editable

        key: None | Unset | str
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if editable is not UNSET:
            field_dict["editable"] = editable
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value")

        editable = d.pop("editable", UNSET)

        def _parse_key(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        key = _parse_key(d.pop("key", UNSET))

        tag = cls(
            value=value,
            editable=editable,
            key=key,
        )

        tag.additional_properties = d
        return tag

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
