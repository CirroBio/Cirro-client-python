from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TaskCost")


@_attrs_define
class TaskCost:
    """
    Attributes:
        name (str):
        task_id (str):
        status (str):
        cost (float):
    """

    name: str
    task_id: str
    status: str
    cost: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        task_id = self.task_id

        status = self.status

        cost = self.cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "taskId": task_id,
                "status": status,
                "cost": cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        task_id = d.pop("taskId")

        status = d.pop("status")

        cost = d.pop("cost")

        task_cost = cls(
            name=name,
            task_id=task_id,
            status=status,
            cost=cost,
        )

        task_cost.additional_properties = d
        return task_cost

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
