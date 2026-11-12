from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sheet_search_hit import SheetSearchHit


T = TypeVar("T", bound="SheetSearchResponse")


@_attrs_define
class SheetSearchResponse:
    """A page of sheet search hits, one per distinct value in a column of a sheet: values equal to the search text first,
    then values starting with it, then the values in the most rows

        Attributes:
            hits (list[SheetSearchHit]):
            total_hits (int | None | Unset): Number of hits across all pages, counting a value once per column of each
                sheet. Null on a page past the last hit.
            total_sheets (int | None | Unset): Number of sheets with at least one hit. Null on a page past the last hit.
    """

    hits: list[SheetSearchHit]
    total_hits: int | None | Unset = UNSET
    total_sheets: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hits = []
        for hits_item_data in self.hits:
            hits_item = hits_item_data.to_dict()
            hits.append(hits_item)

        total_hits: int | None | Unset
        if isinstance(self.total_hits, Unset):
            total_hits = UNSET
        else:
            total_hits = self.total_hits

        total_sheets: int | None | Unset
        if isinstance(self.total_sheets, Unset):
            total_sheets = UNSET
        else:
            total_sheets = self.total_sheets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hits": hits,
            }
        )
        if total_hits is not UNSET:
            field_dict["totalHits"] = total_hits
        if total_sheets is not UNSET:
            field_dict["totalSheets"] = total_sheets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sheet_search_hit import SheetSearchHit

        d = dict(src_dict)
        hits = []
        _hits = d.pop("hits")
        for hits_item_data in _hits:
            hits_item = SheetSearchHit.from_dict(hits_item_data)

            hits.append(hits_item)

        def _parse_total_hits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_hits = _parse_total_hits(d.pop("totalHits", UNSET))

        def _parse_total_sheets(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_sheets = _parse_total_sheets(d.pop("totalSheets", UNSET))

        sheet_search_response = cls(
            hits=hits,
            total_hits=total_hits,
            total_sheets=total_sheets,
        )

        sheet_search_response.additional_properties = d
        return sheet_search_response

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
