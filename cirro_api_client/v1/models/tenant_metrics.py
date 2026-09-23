from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TenantMetrics")


@_attrs_define
class TenantMetrics:
    """
    Attributes:
        project_count (int):
        dataset_count (int):
        pipeline_count (int):
        workspace_count (int):
        user_count (int):
        policy_count (int):
    """

    project_count: int
    dataset_count: int
    pipeline_count: int
    workspace_count: int
    user_count: int
    policy_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_count = self.project_count

        dataset_count = self.dataset_count

        pipeline_count = self.pipeline_count

        workspace_count = self.workspace_count

        user_count = self.user_count

        policy_count = self.policy_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectCount": project_count,
                "datasetCount": dataset_count,
                "pipelineCount": pipeline_count,
                "workspaceCount": workspace_count,
                "userCount": user_count,
                "policyCount": policy_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_count = d.pop("projectCount")

        dataset_count = d.pop("datasetCount")

        pipeline_count = d.pop("pipelineCount")

        workspace_count = d.pop("workspaceCount")

        user_count = d.pop("userCount")

        policy_count = d.pop("policyCount")

        tenant_metrics = cls(
            project_count=project_count,
            dataset_count=dataset_count,
            pipeline_count=pipeline_count,
            workspace_count=workspace_count,
            user_count=user_count,
            policy_count=policy_count,
        )

        tenant_metrics.additional_properties = d
        return tenant_metrics

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
