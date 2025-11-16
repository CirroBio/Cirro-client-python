from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.artifact import Artifact
    from ..models.dataset_viz import DatasetViz
    from ..models.file_entry import FileEntry
    from ..models.table import Table


T = TypeVar("T", bound="DatasetAssetsManifest")


@_attrs_define
class DatasetAssetsManifest:
    """
    Attributes:
        domain (Union[Unset, str]): Base URL for files Example: s3://project-1a1a/datasets/1a1a.
        files (Union[Unset, List['FileEntry']]): List of files in the dataset, including metadata
        total_files (Union[Unset, int]): Total number of files in the dataset, used for pagination
        viz (Union[Unset, List['DatasetViz']]): List of viz to render for the dataset
        tables (Union[Unset, List['Table']]): List of web optimized tables for the dataset
        artifacts (Union[Unset, List['Artifact']]): Artifacts associated with the dataset
    """

    domain: Unset | str = UNSET
    files: Unset | list["FileEntry"] = UNSET
    total_files: Unset | int = UNSET
    viz: Unset | list["DatasetViz"] = UNSET
    tables: Unset | list["Table"] = UNSET
    artifacts: Unset | list["Artifact"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        files: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        total_files = self.total_files

        viz: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.viz, Unset):
            viz = []
            for viz_item_data in self.viz:
                viz_item = viz_item_data.to_dict()
                viz.append(viz_item)

        tables: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.tables, Unset):
            tables = []
            for tables_item_data in self.tables:
                tables_item = tables_item_data.to_dict()
                tables.append(tables_item)

        artifacts: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.artifacts, Unset):
            artifacts = []
            for artifacts_item_data in self.artifacts:
                artifacts_item = artifacts_item_data.to_dict()
                artifacts.append(artifacts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain is not UNSET:
            field_dict["domain"] = domain
        if files is not UNSET:
            field_dict["files"] = files
        if total_files is not UNSET:
            field_dict["totalFiles"] = total_files
        if viz is not UNSET:
            field_dict["viz"] = viz
        if tables is not UNSET:
            field_dict["tables"] = tables
        if artifacts is not UNSET:
            field_dict["artifacts"] = artifacts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.artifact import Artifact
        from ..models.dataset_viz import DatasetViz
        from ..models.file_entry import FileEntry
        from ..models.table import Table

        d = src_dict.copy()
        domain = d.pop("domain", UNSET)

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = FileEntry.from_dict(files_item_data)

            files.append(files_item)

        total_files = d.pop("totalFiles", UNSET)

        viz = []
        _viz = d.pop("viz", UNSET)
        for viz_item_data in _viz or []:
            viz_item = DatasetViz.from_dict(viz_item_data)

            viz.append(viz_item)

        tables = []
        _tables = d.pop("tables", UNSET)
        for tables_item_data in _tables or []:
            tables_item = Table.from_dict(tables_item_data)

            tables.append(tables_item)

        artifacts = []
        _artifacts = d.pop("artifacts", UNSET)
        for artifacts_item_data in _artifacts or []:
            artifacts_item = Artifact.from_dict(artifacts_item_data)

            artifacts.append(artifacts_item)

        dataset_assets_manifest = cls(
            domain=domain,
            files=files,
            total_files=total_files,
            viz=viz,
            tables=tables,
            artifacts=artifacts,
        )

        dataset_assets_manifest.additional_properties = d
        return dataset_assets_manifest

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
