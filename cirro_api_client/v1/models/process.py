import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.executor import Executor
from ..types import UNSET, Unset

T = TypeVar("T", bound="Process")


@_attrs_define
class Process:
    """Identifies a data type or pipeline in Cirro

    Attributes:
        id (str): Unique ID of the Process Example: process-hutch-magic_flute-1_0.
        name (str): Friendly name for the process Example: MAGeCK Flute.
        executor (Executor): How the workflow is executed
        description (Union[Unset, str]): Description of the process Example: MAGeCK Flute enables accurate
            identification of essential genes with their related biological functions.
        data_type (Union[None, Unset, str]): Name of the data type this pipeline produces (if it is not defined, use the
            name)
        category (Union[Unset, str]): Category of the process Example: Microbial Analysis.
        pipeline_type (Union[Unset, str]): Type of pipeline Example: nf-core.
        documentation_url (Union[Unset, str]): Link to process documentation Example:
            https://docs.cirro.bio/pipelines/catalog_targeted_sequencing/#crispr-screen-analysis.
        file_requirements_message (Union[Unset, str]): Description of the files to be uploaded (optional)
        child_process_ids (Union[Unset, List[str]]): IDs of pipelines that can be run downstream
        parent_process_ids (Union[Unset, List[str]]): IDs of processes that can run this pipeline
        owner (Union[None, Unset, str]): Username of the pipeline creator (blank if Cirro curated)
        linked_project_ids (Union[Unset, List[str]]): Projects that can run this process
        is_tenant_wide (Union[Unset, bool]): Whether the process is shared with the tenant
        allow_multiple_sources (Union[Unset, bool]): Whether the pipeline is allowed to have multiple dataset sources
        uses_sample_sheet (Union[Unset, bool]): Whether the pipeline uses the Cirro-provided sample sheet
        is_archived (Union[Unset, bool]): Whether the process is marked as archived
        created_at (Union[Unset, datetime.datetime]): When the process was created (does not reflect the pipeline code)
        updated_at (Union[Unset, datetime.datetime]): When the process was updated (does not reflect the pipeline code)
    """

    id: str
    name: str
    executor: Executor
    description: Union[Unset, str] = UNSET
    data_type: Union[None, Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    pipeline_type: Union[Unset, str] = UNSET
    documentation_url: Union[Unset, str] = UNSET
    file_requirements_message: Union[Unset, str] = UNSET
    child_process_ids: Union[Unset, List[str]] = UNSET
    parent_process_ids: Union[Unset, List[str]] = UNSET
    owner: Union[None, Unset, str] = UNSET
    linked_project_ids: Union[Unset, List[str]] = UNSET
    is_tenant_wide: Union[Unset, bool] = UNSET
    allow_multiple_sources: Union[Unset, bool] = UNSET
    uses_sample_sheet: Union[Unset, bool] = UNSET
    is_archived: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        executor = self.executor.value

        description = self.description

        data_type: Union[None, Unset, str]
        if isinstance(self.data_type, Unset):
            data_type = UNSET
        else:
            data_type = self.data_type

        category = self.category

        pipeline_type = self.pipeline_type

        documentation_url = self.documentation_url

        file_requirements_message = self.file_requirements_message

        child_process_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.child_process_ids, Unset):
            child_process_ids = self.child_process_ids

        parent_process_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.parent_process_ids, Unset):
            parent_process_ids = self.parent_process_ids

        owner: Union[None, Unset, str]
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        linked_project_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.linked_project_ids, Unset):
            linked_project_ids = self.linked_project_ids

        is_tenant_wide = self.is_tenant_wide

        allow_multiple_sources = self.allow_multiple_sources

        uses_sample_sheet = self.uses_sample_sheet

        is_archived = self.is_archived

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "executor": executor,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if category is not UNSET:
            field_dict["category"] = category
        if pipeline_type is not UNSET:
            field_dict["pipelineType"] = pipeline_type
        if documentation_url is not UNSET:
            field_dict["documentationUrl"] = documentation_url
        if file_requirements_message is not UNSET:
            field_dict["fileRequirementsMessage"] = file_requirements_message
        if child_process_ids is not UNSET:
            field_dict["childProcessIds"] = child_process_ids
        if parent_process_ids is not UNSET:
            field_dict["parentProcessIds"] = parent_process_ids
        if owner is not UNSET:
            field_dict["owner"] = owner
        if linked_project_ids is not UNSET:
            field_dict["linkedProjectIds"] = linked_project_ids
        if is_tenant_wide is not UNSET:
            field_dict["isTenantWide"] = is_tenant_wide
        if allow_multiple_sources is not UNSET:
            field_dict["allowMultipleSources"] = allow_multiple_sources
        if uses_sample_sheet is not UNSET:
            field_dict["usesSampleSheet"] = uses_sample_sheet
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        executor = Executor(d.pop("executor"))

        description = d.pop("description", UNSET)

        def _parse_data_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        data_type = _parse_data_type(d.pop("dataType", UNSET))

        category = d.pop("category", UNSET)

        pipeline_type = d.pop("pipelineType", UNSET)

        documentation_url = d.pop("documentationUrl", UNSET)

        file_requirements_message = d.pop("fileRequirementsMessage", UNSET)

        child_process_ids = cast(List[str], d.pop("childProcessIds", UNSET))

        parent_process_ids = cast(List[str], d.pop("parentProcessIds", UNSET))

        def _parse_owner(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        owner = _parse_owner(d.pop("owner", UNSET))

        linked_project_ids = cast(List[str], d.pop("linkedProjectIds", UNSET))

        is_tenant_wide = d.pop("isTenantWide", UNSET)

        allow_multiple_sources = d.pop("allowMultipleSources", UNSET)

        uses_sample_sheet = d.pop("usesSampleSheet", UNSET)

        is_archived = d.pop("isArchived", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        process = cls(
            id=id,
            name=name,
            executor=executor,
            description=description,
            data_type=data_type,
            category=category,
            pipeline_type=pipeline_type,
            documentation_url=documentation_url,
            file_requirements_message=file_requirements_message,
            child_process_ids=child_process_ids,
            parent_process_ids=parent_process_ids,
            owner=owner,
            linked_project_ids=linked_project_ids,
            is_tenant_wide=is_tenant_wide,
            allow_multiple_sources=allow_multiple_sources,
            uses_sample_sheet=uses_sample_sheet,
            is_archived=is_archived,
            created_at=created_at,
            updated_at=updated_at,
        )

        process.additional_properties = d
        return process

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())
