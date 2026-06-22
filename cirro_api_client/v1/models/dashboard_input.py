from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dashboard_input_criteria import DashboardInputCriteria
    from ..models.dashboard_input_dashboard_data import DashboardInputDashboardData
    from ..models.tag import Tag


T = TypeVar("T", bound="DashboardInput")


@_attrs_define
class DashboardInput:
    """
    Attributes:
        name (str):
        description (str):
        dashboard_data (DashboardInputDashboardData):
        criteria (DashboardInputCriteria):
        tags (list[Tag]):
        schema_version (int):
    """

    name: str
    description: str
    dashboard_data: DashboardInputDashboardData
    criteria: DashboardInputCriteria
    tags: list[Tag]
    schema_version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        dashboard_data = self.dashboard_data.to_dict()

        criteria = self.criteria.to_dict()

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        schema_version = self.schema_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "dashboardData": dashboard_data,
                "criteria": criteria,
                "tags": tags,
                "schemaVersion": schema_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_input_criteria import DashboardInputCriteria
        from ..models.dashboard_input_dashboard_data import DashboardInputDashboardData
        from ..models.tag import Tag

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        dashboard_data = DashboardInputDashboardData.from_dict(d.pop("dashboardData"))

        criteria = DashboardInputCriteria.from_dict(d.pop("criteria"))

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = Tag.from_dict(tags_item_data)

            tags.append(tags_item)

        schema_version = d.pop("schemaVersion")

        dashboard_input = cls(
            name=name,
            description=description,
            dashboard_data=dashboard_data,
            criteria=criteria,
            tags=tags,
            schema_version=schema_version,
        )

        dashboard_input.additional_properties = d
        return dashboard_input

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
