from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sheet_job_type import SheetJobType
from ..models.status import Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="SheetJob")


@_attrs_define
class SheetJob:
    """
    Attributes:
        id (str):
        sheet_id (str):
        job_type (SheetJobType):
        status (Status):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        started_at (datetime.datetime | None | Unset):
        completed_at (datetime.datetime | None | Unset):
        failed_at_step (None | str | Unset):
        error_message (None | str | Unset):
        snapshot_id (None | str | Unset):
    """

    id: str
    sheet_id: str
    job_type: SheetJobType
    status: Status
    created_at: datetime.datetime
    updated_at: datetime.datetime
    started_at: datetime.datetime | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    failed_at_step: None | str | Unset = UNSET
    error_message: None | str | Unset = UNSET
    snapshot_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sheet_id = self.sheet_id

        job_type = self.job_type.value

        status = self.status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        failed_at_step: None | str | Unset
        if isinstance(self.failed_at_step, Unset):
            failed_at_step = UNSET
        else:
            failed_at_step = self.failed_at_step

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        snapshot_id: None | str | Unset
        if isinstance(self.snapshot_id, Unset):
            snapshot_id = UNSET
        else:
            snapshot_id = self.snapshot_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sheetId": sheet_id,
                "jobType": job_type,
                "status": status,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if failed_at_step is not UNSET:
            field_dict["failedAtStep"] = failed_at_step
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if snapshot_id is not UNSET:
            field_dict["snapshotId"] = snapshot_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        sheet_id = d.pop("sheetId")

        job_type = SheetJobType(d.pop("jobType"))

        status = Status(d.pop("status"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("startedAt", UNSET))

        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))

        def _parse_failed_at_step(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        failed_at_step = _parse_failed_at_step(d.pop("failedAtStep", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        def _parse_snapshot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        snapshot_id = _parse_snapshot_id(d.pop("snapshotId", UNSET))

        sheet_job = cls(
            id=id,
            sheet_id=sheet_id,
            job_type=job_type,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            started_at=started_at,
            completed_at=completed_at,
            failed_at_step=failed_at_step,
            error_message=error_message,
            snapshot_id=snapshot_id,
        )

        sheet_job.additional_properties = d
        return sheet_job

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
