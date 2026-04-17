from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sheet_creation_mode import SheetCreationMode
from ..models.sheet_type import SheetType
from ..models.status import Status

T = TypeVar("T", bound="Sheet")


@_attrs_define
class Sheet:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        project_id (str):
        sheet_type (SheetType):
        sheet_creation_mode (SheetCreationMode):
        status (Status):
        created_by (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        total_row_count (int):
    """

    id: str
    name: str
    description: str
    project_id: str
    sheet_type: SheetType
    sheet_creation_mode: SheetCreationMode
    status: Status
    created_by: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    total_row_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        project_id = self.project_id

        sheet_type = self.sheet_type.value

        sheet_creation_mode = self.sheet_creation_mode.value

        status = self.status.value

        created_by = self.created_by

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        total_row_count = self.total_row_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "projectId": project_id,
                "sheetType": sheet_type,
                "sheetCreationMode": sheet_creation_mode,
                "status": status,
                "createdBy": created_by,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "totalRowCount": total_row_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        project_id = d.pop("projectId")

        sheet_type = SheetType(d.pop("sheetType"))

        sheet_creation_mode = SheetCreationMode(d.pop("sheetCreationMode"))

        status = Status(d.pop("status"))

        created_by = d.pop("createdBy")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        total_row_count = d.pop("totalRowCount")

        sheet = cls(
            id=id,
            name=name,
            description=description,
            project_id=project_id,
            sheet_type=sheet_type,
            sheet_creation_mode=sheet_creation_mode,
            status=status,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            total_row_count=total_row_count,
        )

        sheet.additional_properties = d
        return sheet

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
