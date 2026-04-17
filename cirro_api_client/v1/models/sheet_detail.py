from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sheet_creation_mode import SheetCreationMode
from ..models.sheet_type import SheetType
from ..models.status import Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_def import ColumnDef
    from ..models.view_query_request import ViewQueryRequest


T = TypeVar("T", bound="SheetDetail")


@_attrs_define
class SheetDetail:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        project_id (str):
        namespace_name (str):
        table_name (str):
        sheet_type (SheetType):
        status (Status):
        audit_read_access (bool):
        created_by (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        total_row_count (int):
        sheet_creation_mode (None | SheetCreationMode | Unset): How the table was initialized. Null for VIEW sheets.
        columns (list[ColumnDef] | None | Unset): Column definitions for the table schema. Null for VIEW sheets.
        view_definition (None | Unset | ViewQueryRequest): View definition for VIEW sheets. Null for TABLE sheets.
        last_refreshed_at (datetime.datetime | None | Unset): When the view was last materialized. Null for TABLE
            sheets.
    """

    id: str
    name: str
    description: str
    project_id: str
    namespace_name: str
    table_name: str
    sheet_type: SheetType
    status: Status
    audit_read_access: bool
    created_by: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    total_row_count: int
    sheet_creation_mode: None | SheetCreationMode | Unset = UNSET
    columns: list[ColumnDef] | None | Unset = UNSET
    view_definition: None | Unset | ViewQueryRequest = UNSET
    last_refreshed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.view_query_request import ViewQueryRequest

        id = self.id

        name = self.name

        description = self.description

        project_id = self.project_id

        namespace_name = self.namespace_name

        table_name = self.table_name

        sheet_type = self.sheet_type.value

        status = self.status.value

        audit_read_access = self.audit_read_access

        created_by = self.created_by

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        total_row_count = self.total_row_count

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

        view_definition: dict[str, Any] | None | Unset
        if isinstance(self.view_definition, Unset):
            view_definition = UNSET
        elif isinstance(self.view_definition, ViewQueryRequest):
            view_definition = self.view_definition.to_dict()
        else:
            view_definition = self.view_definition

        last_refreshed_at: None | str | Unset
        if isinstance(self.last_refreshed_at, Unset):
            last_refreshed_at = UNSET
        elif isinstance(self.last_refreshed_at, datetime.datetime):
            last_refreshed_at = self.last_refreshed_at.isoformat()
        else:
            last_refreshed_at = self.last_refreshed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "projectId": project_id,
                "namespaceName": namespace_name,
                "tableName": table_name,
                "sheetType": sheet_type,
                "status": status,
                "auditReadAccess": audit_read_access,
                "createdBy": created_by,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "totalRowCount": total_row_count,
            }
        )
        if sheet_creation_mode is not UNSET:
            field_dict["sheetCreationMode"] = sheet_creation_mode
        if columns is not UNSET:
            field_dict["columns"] = columns
        if view_definition is not UNSET:
            field_dict["viewDefinition"] = view_definition
        if last_refreshed_at is not UNSET:
            field_dict["lastRefreshedAt"] = last_refreshed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.column_def import ColumnDef
        from ..models.view_query_request import ViewQueryRequest

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        project_id = d.pop("projectId")

        namespace_name = d.pop("namespaceName")

        table_name = d.pop("tableName")

        sheet_type = SheetType(d.pop("sheetType"))

        status = Status(d.pop("status"))

        audit_read_access = d.pop("auditReadAccess")

        created_by = d.pop("createdBy")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        total_row_count = d.pop("totalRowCount")

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

        def _parse_last_refreshed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_refreshed_at_type_0 = isoparse(data)

                return last_refreshed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_refreshed_at = _parse_last_refreshed_at(d.pop("lastRefreshedAt", UNSET))

        sheet_detail = cls(
            id=id,
            name=name,
            description=description,
            project_id=project_id,
            namespace_name=namespace_name,
            table_name=table_name,
            sheet_type=sheet_type,
            status=status,
            audit_read_access=audit_read_access,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            total_row_count=total_row_count,
            sheet_creation_mode=sheet_creation_mode,
            columns=columns,
            view_definition=view_definition,
            last_refreshed_at=last_refreshed_at,
        )

        sheet_detail.additional_properties = d
        return sheet_detail

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
