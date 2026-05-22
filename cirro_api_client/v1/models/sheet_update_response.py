from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sheet_detail import SheetDetail


T = TypeVar("T", bound="SheetUpdateResponse")


@_attrs_define
class SheetUpdateResponse:
    """
    Attributes:
        sheet (SheetDetail | Unset):
        sql_statements (list[str] | Unset): SQL DDL statements applied (TABLE schema changes) or that WOULD be applied
            (dryRun). Empty for metadata-only updates and for VIEW updates.
        changes (list[str] | Unset): Human-readable summary of the changes applied (or that would be applied for
            dryRun). Suitable for showing to users unfamiliar with SQL. Empty for metadata-only and VIEW updates.
    """

    sheet: SheetDetail | Unset = UNSET
    sql_statements: list[str] | Unset = UNSET
    changes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sheet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sheet, Unset):
            sheet = self.sheet.to_dict()

        sql_statements: list[str] | Unset = UNSET
        if not isinstance(self.sql_statements, Unset):
            sql_statements = self.sql_statements

        changes: list[str] | Unset = UNSET
        if not isinstance(self.changes, Unset):
            changes = self.changes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sheet is not UNSET:
            field_dict["sheet"] = sheet
        if sql_statements is not UNSET:
            field_dict["sqlStatements"] = sql_statements
        if changes is not UNSET:
            field_dict["changes"] = changes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sheet_detail import SheetDetail

        d = dict(src_dict)
        _sheet = d.pop("sheet", UNSET)
        sheet: SheetDetail | Unset
        if isinstance(_sheet, Unset):
            sheet = UNSET
        else:
            sheet = SheetDetail.from_dict(_sheet)

        sql_statements = cast(list[str], d.pop("sqlStatements", UNSET))

        changes = cast(list[str], d.pop("changes", UNSET))

        sheet_update_response = cls(
            sheet=sheet,
            sql_statements=sql_statements,
            changes=changes,
        )

        sheet_update_response.additional_properties = d
        return sheet_update_response

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
