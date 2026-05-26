from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.raw_view_query_request import RawViewQueryRequest
    from ..models.structured_view_query_request import StructuredViewQueryRequest
    from ..models.tag import Tag


T = TypeVar("T", bound="ViewSheetInput")


@_attrs_define
class ViewSheetInput:
    """
    Attributes:
        name (str): Display name for the sheet
        namespace_name (str): Namespace containing the sheet's underlying table. Immutable after create. Example:
            alz_cohort.
        table_name (str): Name of the sheet's underlying table. Mutable via update. Example: my_table.
        view_definition (RawViewQueryRequest | StructuredViewQueryRequest): View definition. viewType=STRUCTURED for
            standard builder; viewType=RAW for a SQL SELECT.
        description (None | str | Unset): Optional description of the sheet's purpose or contents
        audit_read_access (bool | Unset): Enable audit logging for read access to this sheet Default: False.
        tags (list[Tag] | Unset): Tags for the sheet
        sheet_type (str | Unset):
    """

    name: str
    namespace_name: str
    table_name: str
    view_definition: RawViewQueryRequest | StructuredViewQueryRequest
    description: None | str | Unset = UNSET
    audit_read_access: bool | Unset = False
    tags: list[Tag] | Unset = UNSET
    sheet_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.raw_view_query_request import RawViewQueryRequest

        name = self.name

        namespace_name = self.namespace_name

        table_name = self.table_name

        view_definition: dict[str, Any]
        if isinstance(self.view_definition, RawViewQueryRequest):
            view_definition = self.view_definition.to_dict()
        else:
            view_definition = self.view_definition.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        audit_read_access = self.audit_read_access

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        sheet_type = self.sheet_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "namespaceName": namespace_name,
                "tableName": table_name,
                "viewDefinition": view_definition,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if audit_read_access is not UNSET:
            field_dict["auditReadAccess"] = audit_read_access
        if tags is not UNSET:
            field_dict["tags"] = tags
        if sheet_type is not UNSET:
            field_dict["sheetType"] = sheet_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_view_query_request import RawViewQueryRequest
        from ..models.structured_view_query_request import StructuredViewQueryRequest
        from ..models.tag import Tag

        d = dict(src_dict)
        name = d.pop("name")

        namespace_name = d.pop("namespaceName")

        table_name = d.pop("tableName")

        def _parse_view_definition(data: object) -> RawViewQueryRequest | StructuredViewQueryRequest:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_view_query_request_type_0 = RawViewQueryRequest.from_dict(data)

                return componentsschemas_view_query_request_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_view_query_request_type_1 = StructuredViewQueryRequest.from_dict(data)

            return componentsschemas_view_query_request_type_1

        view_definition = _parse_view_definition(d.pop("viewDefinition"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        audit_read_access = d.pop("auditReadAccess", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[Tag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = Tag.from_dict(tags_item_data)

                tags.append(tags_item)

        sheet_type = d.pop("sheetType", UNSET)

        view_sheet_input = cls(
            name=name,
            namespace_name=namespace_name,
            table_name=table_name,
            view_definition=view_definition,
            description=description,
            audit_read_access=audit_read_access,
            tags=tags,
            sheet_type=sheet_type,
        )

        view_sheet_input.additional_properties = d
        return view_sheet_input

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
