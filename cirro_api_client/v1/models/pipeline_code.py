from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.repository_type import RepositoryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineCode")


@_attrs_define
class PipelineCode:
    """Used to describe the pipeline analysis code, not required for ingest processes

    Attributes:
        repository_path (str): GitHub repository which contains the workflow code Example: nf-core/rnaseq.
        version (str): Branch, tag, or commit hash of the pipeline code Example: main.
        repository_type (RepositoryType): Type of repository
        entry_point (str): Main script for running the pipeline Example: main.nf.
        executor_version (None | str | Unset): Version of the executor Example: 24.10.5.
    """

    repository_path: str
    version: str
    repository_type: RepositoryType
    entry_point: str
    executor_version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository_path = self.repository_path

        version = self.version

        repository_type = self.repository_type.value

        entry_point = self.entry_point

        executor_version: None | str | Unset
        if isinstance(self.executor_version, Unset):
            executor_version = UNSET
        else:
            executor_version = self.executor_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repositoryPath": repository_path,
                "version": version,
                "repositoryType": repository_type,
                "entryPoint": entry_point,
            }
        )
        if executor_version is not UNSET:
            field_dict["executorVersion"] = executor_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repository_path = d.pop("repositoryPath")

        version = d.pop("version")

        repository_type = RepositoryType(d.pop("repositoryType"))

        entry_point = d.pop("entryPoint")

        def _parse_executor_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        executor_version = _parse_executor_version(d.pop("executorVersion", UNSET))

        pipeline_code = cls(
            repository_path=repository_path,
            version=version,
            repository_type=repository_type,
            entry_point=entry_point,
            executor_version=executor_version,
        )

        pipeline_code.additional_properties = d
        return pipeline_code

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
