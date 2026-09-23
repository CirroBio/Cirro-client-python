from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_mode import ExecutionMode
from ..models.executor import Executor
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tag import Tag


T = TypeVar("T", bound="Process")


@_attrs_define
class Process:
    """Identifies a data type or pipeline in Cirro

    Attributes:
        id (str): Unique ID of the Process Example: process-hutch-magic_flute-1_0.
        name (str): Friendly name for the process Example: MAGeCK Flute.
        description (str): Description of the process Example: MAGeCK Flute enables accurate identification of essential
            genes with their related biological functions.
        data_type (str): Name of the data type this pipeline produces (if it is not defined, use the name)
        executor (Executor): How the workflow is executed
        child_process_ids (list[str]): IDs of pipelines that can be run downstream
        parent_process_ids (list[str]): IDs of processes that can run this pipeline
        linked_project_ids (list[str]): Projects that can run this process
        is_tenant_wide (bool): Whether the process is shared with the tenant
        allow_multiple_sources (bool): Whether the pipeline is allowed to have multiple dataset sources
        uses_sample_sheet (bool): Whether the pipeline uses the Cirro-provided sample sheet
        execution_modes (list[ExecutionMode]): Execution modes the pipeline supports
        is_archived (bool): Whether the process is marked as archived
        tags (list[Tag]):
        category (str | Unset): Category of the process Example: Microbial Analysis.
        pipeline_type (str | Unset): Type of pipeline Example: nf-core.
        documentation_url (str | Unset): Link to process documentation Example:
            https://docs.cirro.bio/pipelines/catalog_targeted_sequencing/#crispr-screen-analysis.
        file_requirements_message (str | Unset): Description of the files to be uploaded (optional)
        owner (None | str | Unset): Username of the pipeline creator (blank if Cirro curated)
        maintainers (list[str] | None | Unset): Other users who maintain the pipeline. These users have access to manage
            the pipeline (blank if Cirro curated)
        created_at (datetime.datetime | Unset): When the process was created (does not reflect the pipeline code)
        updated_at (datetime.datetime | Unset): When the process was updated (does not reflect the pipeline code)
    """

    id: str
    name: str
    description: str
    data_type: str
    executor: Executor
    child_process_ids: list[str]
    parent_process_ids: list[str]
    linked_project_ids: list[str]
    is_tenant_wide: bool
    allow_multiple_sources: bool
    uses_sample_sheet: bool
    execution_modes: list[ExecutionMode]
    is_archived: bool
    tags: list[Tag]
    category: str | Unset = UNSET
    pipeline_type: str | Unset = UNSET
    documentation_url: str | Unset = UNSET
    file_requirements_message: str | Unset = UNSET
    owner: None | str | Unset = UNSET
    maintainers: list[str] | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        data_type = self.data_type

        executor = self.executor.value

        child_process_ids = self.child_process_ids

        parent_process_ids = self.parent_process_ids

        linked_project_ids = self.linked_project_ids

        is_tenant_wide = self.is_tenant_wide

        allow_multiple_sources = self.allow_multiple_sources

        uses_sample_sheet = self.uses_sample_sheet

        execution_modes = []
        for execution_modes_item_data in self.execution_modes:
            execution_modes_item = execution_modes_item_data.value
            execution_modes.append(execution_modes_item)

        is_archived = self.is_archived

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        category = self.category

        pipeline_type = self.pipeline_type

        documentation_url = self.documentation_url

        file_requirements_message = self.file_requirements_message

        owner: None | str | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        maintainers: list[str] | None | Unset
        if isinstance(self.maintainers, Unset):
            maintainers = UNSET
        elif isinstance(self.maintainers, list):
            maintainers = self.maintainers

        else:
            maintainers = self.maintainers

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "dataType": data_type,
                "executor": executor,
                "childProcessIds": child_process_ids,
                "parentProcessIds": parent_process_ids,
                "linkedProjectIds": linked_project_ids,
                "isTenantWide": is_tenant_wide,
                "allowMultipleSources": allow_multiple_sources,
                "usesSampleSheet": uses_sample_sheet,
                "executionModes": execution_modes,
                "isArchived": is_archived,
                "tags": tags,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if pipeline_type is not UNSET:
            field_dict["pipelineType"] = pipeline_type
        if documentation_url is not UNSET:
            field_dict["documentationUrl"] = documentation_url
        if file_requirements_message is not UNSET:
            field_dict["fileRequirementsMessage"] = file_requirements_message
        if owner is not UNSET:
            field_dict["owner"] = owner
        if maintainers is not UNSET:
            field_dict["maintainers"] = maintainers
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tag import Tag

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        data_type = d.pop("dataType")

        executor = Executor(d.pop("executor"))

        child_process_ids = cast(list[str], d.pop("childProcessIds"))

        parent_process_ids = cast(list[str], d.pop("parentProcessIds"))

        linked_project_ids = cast(list[str], d.pop("linkedProjectIds"))

        is_tenant_wide = d.pop("isTenantWide")

        allow_multiple_sources = d.pop("allowMultipleSources")

        uses_sample_sheet = d.pop("usesSampleSheet")

        execution_modes = []
        _execution_modes = d.pop("executionModes")
        for execution_modes_item_data in _execution_modes:
            execution_modes_item = ExecutionMode(execution_modes_item_data)

            execution_modes.append(execution_modes_item)

        is_archived = d.pop("isArchived")

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = Tag.from_dict(tags_item_data)

            tags.append(tags_item)

        category = d.pop("category", UNSET)

        pipeline_type = d.pop("pipelineType", UNSET)

        documentation_url = d.pop("documentationUrl", UNSET)

        file_requirements_message = d.pop("fileRequirementsMessage", UNSET)

        def _parse_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        def _parse_maintainers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                maintainers_type_0 = cast(list[str], data)

                return maintainers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        maintainers = _parse_maintainers(d.pop("maintainers", UNSET))

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        process = cls(
            id=id,
            name=name,
            description=description,
            data_type=data_type,
            executor=executor,
            child_process_ids=child_process_ids,
            parent_process_ids=parent_process_ids,
            linked_project_ids=linked_project_ids,
            is_tenant_wide=is_tenant_wide,
            allow_multiple_sources=allow_multiple_sources,
            uses_sample_sheet=uses_sample_sheet,
            execution_modes=execution_modes,
            is_archived=is_archived,
            tags=tags,
            category=category,
            pipeline_type=pipeline_type,
            documentation_url=documentation_url,
            file_requirements_message=file_requirements_message,
            owner=owner,
            maintainers=maintainers,
            created_at=created_at,
            updated_at=updated_at,
        )

        process.additional_properties = d
        return process

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
