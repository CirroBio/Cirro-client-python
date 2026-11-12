from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SheetDiffRequest")


@_attrs_define
class SheetDiffRequest:
    """Paginated row changes between two snapshots of a TABLE sheet

    Attributes:
        from_snapshot_id (str): Snapshot the changes start from, usually the older one.
        to_snapshot_id (str): Snapshot the changes lead to, usually the newer one.
        limit (int | None | Unset): Maximum changed rows to return. An UPDATED row comes back in both before and after,
            and responses have a size limit: with wide rows a large page can fail with a 502 — lower the limit if so.
            Default: 1000.
        page (int | None | Unset): Page to return Default: 1.
    """

    from_snapshot_id: str
    to_snapshot_id: str
    limit: int | None | Unset = 1000
    page: int | None | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_snapshot_id = self.from_snapshot_id

        to_snapshot_id = self.to_snapshot_id

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        page: int | None | Unset
        if isinstance(self.page, Unset):
            page = UNSET
        else:
            page = self.page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fromSnapshotId": from_snapshot_id,
                "toSnapshotId": to_snapshot_id,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit
        if page is not UNSET:
            field_dict["page"] = page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_snapshot_id = d.pop("fromSnapshotId")

        to_snapshot_id = d.pop("toSnapshotId")

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        def _parse_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page = _parse_page(d.pop("page", UNSET))

        sheet_diff_request = cls(
            from_snapshot_id=from_snapshot_id,
            to_snapshot_id=to_snapshot_id,
            limit=limit,
            page=page,
        )

        sheet_diff_request.additional_properties = d
        return sheet_diff_request

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
