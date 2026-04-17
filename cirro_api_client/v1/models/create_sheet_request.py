from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sheet_creation_mode import SheetCreationMode
from ..models.sheet_type import SheetType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_def import ColumnDef
    from ..models.file_def import FileDef
    from ..models.view_query_request import ViewQueryRequest


T = TypeVar("T", bound="CreateSheetRequest")


@_attrs_define
class CreateSheetRequest:
    """
    Attributes:
        name (str): Display name for the sheet
        namespace_name (str): Namespace for the sheet. This serves as a container to group and manage sheets.
            Permissions can be broadly managed at this level too. Example: alz_cohort.
        table_name (str): Name of the sheet's underlying table Example: my_table.
        sheet_type (SheetType):
        description (str | Unset): Optional description of the sheet's purpose or contents
        audit_read_access (bool | Unset): Enable audit logging for read access to this sheet Default: False.
        sheet_creation_mode (None | SheetCreationMode | Unset): How the table should be initialized (required for TABLE)
        columns (list[ColumnDef] | None | Unset): Column definitions for the table schema (required for TABLE)
        file_def (FileDef | None | Unset): If provided, an ingest job is triggered immediately after table creation
            (TABLE only)
        view_definition (None | Unset | ViewQueryRequest): View definition specifying sheets, joins, columns, and
            filters (required for VIEW)
    """

    name: str
    namespace_name: str
    table_name: str
    sheet_type: SheetType
    description: str | Unset = UNSET
    audit_read_access: bool | Unset = False
    sheet_creation_mode: None | SheetCreationMode | Unset = UNSET
    columns: list[ColumnDef] | None | Unset = UNSET
    file_def: FileDef | None | Unset = UNSET
    view_definition: None | Unset | ViewQueryRequest = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.file_def import FileDef
        from ..models.view_query_request import ViewQueryRequest

        name = self.name

        namespace_name = self.namespace_name

        table_name = self.table_name

        sheet_type = self.sheet_type.value

        description = self.description

        audit_read_access = self.audit_read_access

        sheet_creation_mode: None | str | Unset
        if isinstance(self.sheet_creation_mode, Unset):
            sheet_creation_mode = UNSET
        elif isinstance(self.sheet_creation_mode, SheetCreationMode):
            sheet_creation_mode = self.sheet_creation_mode.value
        else:
            sheet_creation_mode = self.sheet_creation_mode

        columns: list[dict[str, Any]] | None | Unset
        if isinstance(self.columns, Unset):
            columns = UNSET
        elif isinstance(self.columns, list):
            columns = []
            for columns_type_0_item_data in self.columns:
                columns_type_0_item = columns_type_0_item_data.to_dict()
                columns.append(columns_type_0_item)

        else:
            columns = self.columns

        file_def: dict[str, Any] | None | Unset
        if isinstance(self.file_def, Unset):
            file_def = UNSET
        elif isinstance(self.file_def, FileDef):
            file_def = self.file_def.to_dict()
        else:
            file_def = self.file_def

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
                "namespaceName": namespace_name,
                "tableName": table_name,
                "sheetType": sheet_type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if audit_read_access is not UNSET:
            field_dict["auditReadAccess"] = audit_read_access
        if sheet_creation_mode is not UNSET:
            field_dict["sheetCreationMode"] = sheet_creation_mode
        if columns is not UNSET:
            field_dict["columns"] = columns
        if file_def is not UNSET:
            field_dict["fileDef"] = file_def
        if view_definition is not UNSET:
            field_dict["viewDefinition"] = view_definition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.column_def import ColumnDef
        from ..models.file_def import FileDef
        from ..models.view_query_request import ViewQueryRequest

        d = dict(src_dict)
        name = d.pop("name")

        namespace_name = d.pop("namespaceName")

        table_name = d.pop("tableName")

        sheet_type = SheetType(d.pop("sheetType"))

        description = d.pop("description", UNSET)

        audit_read_access = d.pop("auditReadAccess", UNSET)

        def _parse_sheet_creation_mode(data: object) -> None | SheetCreationMode | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sheet_creation_mode_type_1 = SheetCreationMode(data)

                return sheet_creation_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SheetCreationMode | Unset, data)

        sheet_creation_mode = _parse_sheet_creation_mode(d.pop("sheetCreationMode", UNSET))

        def _parse_columns(data: object) -> list[ColumnDef] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                columns_type_0 = []
                _columns_type_0 = data
                for columns_type_0_item_data in _columns_type_0:
                    columns_type_0_item = ColumnDef.from_dict(columns_type_0_item_data)

                    columns_type_0.append(columns_type_0_item)

                return columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ColumnDef] | None | Unset, data)

        columns = _parse_columns(d.pop("columns", UNSET))

        def _parse_file_def(data: object) -> FileDef | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                file_def_type_1 = FileDef.from_dict(data)

                return file_def_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FileDef | None | Unset, data)

        file_def = _parse_file_def(d.pop("fileDef", UNSET))

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

        create_sheet_request = cls(
            name=name,
            namespace_name=namespace_name,
            table_name=table_name,
            sheet_type=sheet_type,
            description=description,
            audit_read_access=audit_read_access,
            sheet_creation_mode=sheet_creation_mode,
            columns=columns,
            file_def=file_def,
            view_definition=view_definition,
        )

        create_sheet_request.additional_properties = d
        return create_sheet_request

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
