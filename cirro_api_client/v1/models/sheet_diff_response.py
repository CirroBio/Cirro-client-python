from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sheet_query_response import SheetQueryResponse
    from ..models.sheet_row_change import SheetRowChange


T = TypeVar("T", bound="SheetDiffResponse")


@_attrs_define
class SheetDiffResponse:
    """Paginated row changes between two snapshots of a TABLE sheet, matched by `_row_id`.
    `changes` lists this page's changes; `before` and `after` hold the row data for them, keyed by `_row_id`.

        Attributes:
            changes (list[SheetRowChange]): This page's changes, ordered by `_row_id`. Paging, the limit and `totalRowCount`
                count these.
            before (SheetQueryResponse): Paginated query result from a sheet.
                The first column is always `_row_id` which uniquely identifies each row.
                Clients should use this value when calling the update endpoint (`PUT
                /projects/{projectId}/sheets/{sheetId}/data`)
            after (SheetQueryResponse): Paginated query result from a sheet.
                The first column is always `_row_id` which uniquely identifies each row.
                Clients should use this value when calling the update endpoint (`PUT
                /projects/{projectId}/sheets/{sheetId}/data`)
            total_row_count (int): Number of changes across all pages.
    """

    changes: list[SheetRowChange]
    before: SheetQueryResponse
    after: SheetQueryResponse
    total_row_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changes = []
        for changes_item_data in self.changes:
            changes_item = changes_item_data.to_dict()
            changes.append(changes_item)

        before = self.before.to_dict()

        after = self.after.to_dict()

        total_row_count = self.total_row_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changes": changes,
                "before": before,
                "after": after,
                "totalRowCount": total_row_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sheet_query_response import SheetQueryResponse
        from ..models.sheet_row_change import SheetRowChange

        d = dict(src_dict)
        changes = []
        _changes = d.pop("changes")
        for changes_item_data in _changes:
            changes_item = SheetRowChange.from_dict(changes_item_data)

            changes.append(changes_item)

        before = SheetQueryResponse.from_dict(d.pop("before"))

        after = SheetQueryResponse.from_dict(d.pop("after"))

        total_row_count = d.pop("totalRowCount")

        sheet_diff_response = cls(
            changes=changes,
            before=before,
            after=after,
            total_row_count=total_row_count,
        )

        sheet_diff_response.additional_properties = d
        return sheet_diff_response

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
