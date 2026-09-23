from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_file import ProjectFile


T = TypeVar("T", bound="ProjectFileQueryResponse")


@_attrs_define
class ProjectFileQueryResponse:
    """
    Attributes:
        data (list[ProjectFile]):
        next_token (None | str | Unset): Token used to fetch the next page; null when there are no more results
        total_count (int | None | Unset): Total number of files matching the query; only populated on the first page
    """

    data: list[ProjectFile]
    next_token: None | str | Unset = UNSET
    total_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        next_token: None | str | Unset
        if isinstance(self.next_token, Unset):
            next_token = UNSET
        else:
            next_token = self.next_token

        total_count: int | None | Unset
        if isinstance(self.total_count, Unset):
            total_count = UNSET
        else:
            total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if next_token is not UNSET:
            field_dict["nextToken"] = next_token
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_file import ProjectFile

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ProjectFile.from_dict(data_item_data)

            data.append(data_item)

        def _parse_next_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_token = _parse_next_token(d.pop("nextToken", UNSET))

        def _parse_total_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_count = _parse_total_count(d.pop("totalCount", UNSET))

        project_file_query_response = cls(
            data=data,
            next_token=next_token,
            total_count=total_count,
        )

        project_file_query_response.additional_properties = d
        return project_file_query_response

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
