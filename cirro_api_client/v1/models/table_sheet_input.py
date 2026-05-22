from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sheet_creation_mode import SheetCreationMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_def import ColumnDef
    from ..models.tag import Tag


T = TypeVar("T", bound="TableSheetInput")


@_attrs_define
class TableSheetInput:
    """
    Attributes:
        name (str): Display name for the sheet
        namespace_name (str): Namespace containing the sheet's underlying table. Immutable after create. Example:
            alz_cohort.
        table_name (str): Name of the sheet's underlying table. Mutable via update. Example: my_table.
        sheet_creation_mode (SheetCreationMode):
        columns (list[ColumnDef]): Target column list for the sheet. On update, the server computes the diff against
            existing columns (matched by column id) and applies the resulting ADD/DROP/RENAME/TYPE changes as a single
            transactional ALTER sequence. Existing columns include their id; new columns omit it.
        description (None | str | Unset): Optional description of the sheet's purpose or contents
        audit_read_access (bool | Unset): Enable audit logging for read access to this sheet Default: False.
        schema_version_id (int | None | Unset): Current table schema version (starts at 0). Used for optimistic
            concurrency control. New tables can omit this, but updates should include this to prevent overwriting due to
            stale table schema metadata.
        tags (list[Tag] | Unset): Tags for the sheet
        sheet_type (str | Unset):
    """

    name: str
    namespace_name: str
    table_name: str
    sheet_creation_mode: SheetCreationMode
    columns: list[ColumnDef]
    description: None | str | Unset = UNSET
    audit_read_access: bool | Unset = False
    schema_version_id: int | None | Unset = UNSET
    tags: list[Tag] | Unset = UNSET
    sheet_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        namespace_name = self.namespace_name

        table_name = self.table_name

        sheet_creation_mode = self.sheet_creation_mode.value

        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        audit_read_access = self.audit_read_access

        schema_version_id: int | None | Unset
        if isinstance(self.schema_version_id, Unset):
            schema_version_id = UNSET
        else:
            schema_version_id = self.schema_version_id

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
                "sheetCreationMode": sheet_creation_mode,
                "columns": columns,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if audit_read_access is not UNSET:
            field_dict["auditReadAccess"] = audit_read_access
        if schema_version_id is not UNSET:
            field_dict["schemaVersionId"] = schema_version_id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if sheet_type is not UNSET:
            field_dict["sheetType"] = sheet_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.column_def import ColumnDef
        from ..models.tag import Tag

        d = dict(src_dict)
        name = d.pop("name")

        namespace_name = d.pop("namespaceName")

        table_name = d.pop("tableName")

        sheet_creation_mode = SheetCreationMode(d.pop("sheetCreationMode"))

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = ColumnDef.from_dict(columns_item_data)

            columns.append(columns_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        audit_read_access = d.pop("auditReadAccess", UNSET)

        def _parse_schema_version_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        schema_version_id = _parse_schema_version_id(d.pop("schemaVersionId", UNSET))

        _tags = d.pop("tags", UNSET)
        tags: list[Tag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = Tag.from_dict(tags_item_data)

                tags.append(tags_item)

        sheet_type = d.pop("sheetType", UNSET)

        table_sheet_input = cls(
            name=name,
            namespace_name=namespace_name,
            table_name=table_name,
            sheet_creation_mode=sheet_creation_mode,
            columns=columns,
            description=description,
            audit_read_access=audit_read_access,
            schema_version_id=schema_version_id,
            tags=tags,
            sheet_type=sheet_type,
        )

        table_sheet_input.additional_properties = d
        return table_sheet_input

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
