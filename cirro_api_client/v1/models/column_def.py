from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.column_data_type import ColumnDataType
from ..models.semantic_column_type import SemanticColumnType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.foreign_key_ref import ForeignKeyRef


T = TypeVar("T", bound="ColumnDef")


@_attrs_define
class ColumnDef:
    """
    Attributes:
        name (str):
        data_type (ColumnDataType): Data type for the column.
        id (None | str | Unset):
        display_name (None | str | Unset): Name displayed on UI.
        hidden (bool | Unset): Whether the column is hidden on the UI. Default: False.
        semantic_type (None | SemanticColumnType | Unset): The semantic type of the column. Default:
            SemanticColumnType.STANDARD.
        allowed_values (list[str] | None | Unset): The allowed values for the column, only used for ENUM* types.
        description (None | str | Unset):
        foreign_key (ForeignKeyRef | None | Unset):
        required (bool | Unset): Whether the column is required to be non-null. Default: False.
    """

    name: str
    data_type: ColumnDataType
    id: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    hidden: bool | Unset = False
    semantic_type: None | SemanticColumnType | Unset = SemanticColumnType.STANDARD
    allowed_values: list[str] | None | Unset = UNSET
    description: None | str | Unset = UNSET
    foreign_key: ForeignKeyRef | None | Unset = UNSET
    required: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.foreign_key_ref import ForeignKeyRef

        name = self.name

        data_type = self.data_type.value

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        hidden = self.hidden

        semantic_type: None | str | Unset
        if isinstance(self.semantic_type, Unset):
            semantic_type = UNSET
        elif isinstance(self.semantic_type, SemanticColumnType):
            semantic_type = self.semantic_type.value
        else:
            semantic_type = self.semantic_type

        allowed_values: list[str] | None | Unset
        if isinstance(self.allowed_values, Unset):
            allowed_values = UNSET
        elif isinstance(self.allowed_values, list):
            allowed_values = self.allowed_values

        else:
            allowed_values = self.allowed_values

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        foreign_key: dict[str, Any] | None | Unset
        if isinstance(self.foreign_key, Unset):
            foreign_key = UNSET
        elif isinstance(self.foreign_key, ForeignKeyRef):
            foreign_key = self.foreign_key.to_dict()
        else:
            foreign_key = self.foreign_key

        required = self.required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "dataType": data_type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if semantic_type is not UNSET:
            field_dict["semanticType"] = semantic_type
        if allowed_values is not UNSET:
            field_dict["allowedValues"] = allowed_values
        if description is not UNSET:
            field_dict["description"] = description
        if foreign_key is not UNSET:
            field_dict["foreignKey"] = foreign_key
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.foreign_key_ref import ForeignKeyRef

        d = dict(src_dict)
        name = d.pop("name")

        data_type = ColumnDataType(d.pop("dataType"))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        hidden = d.pop("hidden", UNSET)

        def _parse_semantic_type(data: object) -> None | SemanticColumnType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                semantic_type_type_1 = SemanticColumnType(data)

                return semantic_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SemanticColumnType | Unset, data)

        semantic_type = _parse_semantic_type(d.pop("semanticType", UNSET))

        def _parse_allowed_values(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_values_type_0 = cast(list[str], data)

                return allowed_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_values = _parse_allowed_values(d.pop("allowedValues", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        required = d.pop("required", UNSET)

        column_def = cls(
            name=name,
            data_type=data_type,
            id=id,
            display_name=display_name,
            hidden=hidden,
            semantic_type=semantic_type,
            allowed_values=allowed_values,
            description=description,
            foreign_key=foreign_key,
            required=required,
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
