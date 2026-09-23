from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cost_component import CostComponent
from ..models.cost_source import CostSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_cost import GroupCost
    from ..models.task_cost import TaskCost


T = TypeVar("T", bound="CostResponse")


@_attrs_define
class CostResponse:
    """
    Attributes:
        total_cost (float | Unset): Total cost
        groups (list[GroupCost] | Unset): Costs grouped by the task status
        tasks (list[TaskCost] | Unset): Costs for each workflow task
        is_estimate (bool | Unset): Whether this is an estimated cost
        storage_cost (float | None | Unset): Run storage cost, included in totalCost; null when not reported by the
            billing source
        cost_source (CostSource | Unset): How a cost was derived
        omitted_components (list[CostComponent] | None | Unset): Billed components known to be excluded from totalCost
            (e.g. run storage when usage was not reported)
    """

    total_cost: float | Unset = UNSET
    groups: list[GroupCost] | Unset = UNSET
    tasks: list[TaskCost] | Unset = UNSET
    is_estimate: bool | Unset = UNSET
    storage_cost: float | None | Unset = UNSET
    cost_source: CostSource | Unset = UNSET
    omitted_components: list[CostComponent] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_cost = self.total_cost

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        tasks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()
                tasks.append(tasks_item)

        is_estimate = self.is_estimate

        storage_cost: float | None | Unset
        if isinstance(self.storage_cost, Unset):
            storage_cost = UNSET
        else:
            storage_cost = self.storage_cost

        cost_source: str | Unset = UNSET
        if not isinstance(self.cost_source, Unset):
            cost_source = self.cost_source.value

        omitted_components: list[str] | None | Unset
        if isinstance(self.omitted_components, Unset):
            omitted_components = UNSET
        elif isinstance(self.omitted_components, list):
            omitted_components = []
            for omitted_components_type_0_item_data in self.omitted_components:
                omitted_components_type_0_item = omitted_components_type_0_item_data.value
                omitted_components.append(omitted_components_type_0_item)

        else:
            omitted_components = self.omitted_components

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_cost is not UNSET:
            field_dict["totalCost"] = total_cost
        if groups is not UNSET:
            field_dict["groups"] = groups
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if is_estimate is not UNSET:
            field_dict["isEstimate"] = is_estimate
        if storage_cost is not UNSET:
            field_dict["storageCost"] = storage_cost
        if cost_source is not UNSET:
            field_dict["costSource"] = cost_source
        if omitted_components is not UNSET:
            field_dict["omittedComponents"] = omitted_components

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_cost import GroupCost
        from ..models.task_cost import TaskCost

        d = dict(src_dict)
        total_cost = d.pop("totalCost", UNSET)

        _groups = d.pop("groups", UNSET)
        groups: list[GroupCost] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = GroupCost.from_dict(groups_item_data)

                groups.append(groups_item)

        _tasks = d.pop("tasks", UNSET)
        tasks: list[TaskCost] | Unset = UNSET
        if _tasks is not UNSET:
            tasks = []
            for tasks_item_data in _tasks:
                tasks_item = TaskCost.from_dict(tasks_item_data)

                tasks.append(tasks_item)

        is_estimate = d.pop("isEstimate", UNSET)

        def _parse_storage_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        storage_cost = _parse_storage_cost(d.pop("storageCost", UNSET))

        _cost_source = d.pop("costSource", UNSET)
        cost_source: CostSource | Unset
        if isinstance(_cost_source, Unset):
            cost_source = UNSET
        else:
            cost_source = CostSource(_cost_source)

        def _parse_omitted_components(data: object) -> list[CostComponent] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                omitted_components_type_0 = []
                _omitted_components_type_0 = data
                for omitted_components_type_0_item_data in _omitted_components_type_0:
                    omitted_components_type_0_item = CostComponent(omitted_components_type_0_item_data)

                    omitted_components_type_0.append(omitted_components_type_0_item)

                return omitted_components_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CostComponent] | None | Unset, data)

        omitted_components = _parse_omitted_components(d.pop("omittedComponents", UNSET))

        cost_response = cls(
            total_cost=total_cost,
            groups=groups,
            tasks=tasks,
            is_estimate=is_estimate,
            storage_cost=storage_cost,
            cost_source=cost_source,
            omitted_components=omitted_components,
        )

        cost_response.additional_properties = d
        return cost_response

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
