from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.column_data_type import ColumnDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.foreign_key_ref import ForeignKeyRef


T = TypeVar("T", bound="ColumnDef")


@_attrs_define
class ColumnDef:
    """
    Attributes:
        name (str):
        data_type (ColumnDataType):
        description (str):
        foreign_key (ForeignKeyRef | None | Unset):
    """

    name: str
    data_type: ColumnDataType
    description: str
    foreign_key: ForeignKeyRef | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.foreign_key_ref import ForeignKeyRef

        name = self.name

        data_type = self.data_type.value

        description = self.description

        foreign_key: dict[str, Any] | None | Unset
        if isinstance(self.foreign_key, Unset):
            foreign_key = UNSET
        elif isinstance(self.foreign_key, ForeignKeyRef):
            foreign_key = self.foreign_key.to_dict()
        else:
            foreign_key = self.foreign_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "dataType": data_type,
                "description": description,
            }
        )
        if foreign_key is not UNSET:
            field_dict["foreignKey"] = foreign_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.foreign_key_ref import ForeignKeyRef

        d = dict(src_dict)
        name = d.pop("name")

        data_type = ColumnDataType(d.pop("dataType"))

        description = d.pop("description")

        def _parse_foreign_key(data: object) -> ForeignKeyRef | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                foreign_key_type_1 = ForeignKeyRef.from_dict(data)

                return foreign_key_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ForeignKeyRef | None | Unset, data)

        foreign_key = _parse_foreign_key(d.pop("foreignKey", UNSET))

        column_def = cls(
            name=name,
            data_type=data_type,
            description=description,
            foreign_key=foreign_key,
        )

        column_def.additional_properties = d
        return column_def

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
