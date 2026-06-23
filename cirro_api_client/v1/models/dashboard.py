from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_criteria import DashboardCriteria
    from ..models.dashboard_data import DashboardData
    from ..models.tag import Tag


T = TypeVar("T", bound="Dashboard")


@_attrs_define
class Dashboard:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        tags (list[Tag]):
        created_by (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        criteria (DashboardCriteria | Unset):
        dashboard_data (DashboardData | None | Unset): Dashboard definition (not provided in list responses)
        schema_version (int | Unset): Schema version of dashboardData
    """

    id: str
    name: str
    description: str
    tags: list[Tag]
    created_by: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    criteria: DashboardCriteria | Unset = UNSET
    dashboard_data: DashboardData | None | Unset = UNSET
    schema_version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_data import DashboardData

        id = self.id

        name = self.name

        description = self.description

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        created_by = self.created_by

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        criteria: dict[str, Any] | Unset = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.to_dict()

        dashboard_data: dict[str, Any] | None | Unset
        if isinstance(self.dashboard_data, Unset):
            dashboard_data = UNSET
        elif isinstance(self.dashboard_data, DashboardData):
            dashboard_data = self.dashboard_data.to_dict()
        else:
            dashboard_data = self.dashboard_data

        schema_version = self.schema_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "tags": tags,
                "createdBy": created_by,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if dashboard_data is not UNSET:
            field_dict["dashboardData"] = dashboard_data
        if schema_version is not UNSET:
            field_dict["schemaVersion"] = schema_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_criteria import DashboardCriteria
        from ..models.dashboard_data import DashboardData
        from ..models.tag import Tag

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = Tag.from_dict(tags_item_data)

            tags.append(tags_item)

        created_by = d.pop("createdBy")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        _criteria = d.pop("criteria", UNSET)
        criteria: DashboardCriteria | Unset
        if isinstance(_criteria, Unset):
            criteria = UNSET
        else:
            criteria = DashboardCriteria.from_dict(_criteria)

        def _parse_dashboard_data(data: object) -> DashboardData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dashboard_data_type_0 = DashboardData.from_dict(data)

                return dashboard_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardData | None | Unset, data)

        dashboard_data = _parse_dashboard_data(d.pop("dashboardData", UNSET))

        schema_version = d.pop("schemaVersion", UNSET)

        dashboard = cls(
            id=id,
            name=name,
            description=description,
            tags=tags,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            criteria=criteria,
            dashboard_data=dashboard_data,
            schema_version=schema_version,
        )

        dashboard.additional_properties = d
        return dashboard

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
