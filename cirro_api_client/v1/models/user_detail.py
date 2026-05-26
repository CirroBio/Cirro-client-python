from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_project_assignment import UserProjectAssignment
    from ..models.user_settings import UserSettings


T = TypeVar("T", bound="UserDetail")


@_attrs_define
class UserDetail:
    """
    Attributes:
        username (str):
        name (str):
        email (str):
        organization (str):
        project_assignments (list[UserProjectAssignment]):
        global_roles (list[str]):
        settings (UserSettings): Additional settings for the user
        phone (None | str | Unset):
        orcid_id (None | str | Unset):
        job_title (None | str | Unset):
        department (None | str | Unset):
        invited_by (None | str | Unset):
        sign_up_time (datetime.datetime | None | Unset):
        last_signed_in (datetime.datetime | None | Unset):
        groups (list[str] | None | Unset): Replaced by globalRoles.
    """

    username: str
    name: str
    email: str
    organization: str
    project_assignments: list[UserProjectAssignment]
    global_roles: list[str]
    settings: UserSettings
    phone: None | str | Unset = UNSET
    orcid_id: None | str | Unset = UNSET
    job_title: None | str | Unset = UNSET
    department: None | str | Unset = UNSET
    invited_by: None | str | Unset = UNSET
    sign_up_time: datetime.datetime | None | Unset = UNSET
    last_signed_in: datetime.datetime | None | Unset = UNSET
    groups: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        name = self.name

        email = self.email

        organization = self.organization

        project_assignments = []
        for project_assignments_item_data in self.project_assignments:
            project_assignments_item = project_assignments_item_data.to_dict()
            project_assignments.append(project_assignments_item)

        global_roles = self.global_roles

        settings = self.settings.to_dict()

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        orcid_id: None | str | Unset
        if isinstance(self.orcid_id, Unset):
            orcid_id = UNSET
        else:
            orcid_id = self.orcid_id

        job_title: None | str | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        else:
            job_title = self.job_title

        department: None | str | Unset
        if isinstance(self.department, Unset):
            department = UNSET
        else:
            department = self.department

        invited_by: None | str | Unset
        if isinstance(self.invited_by, Unset):
            invited_by = UNSET
        else:
            invited_by = self.invited_by

        sign_up_time: None | str | Unset
        if isinstance(self.sign_up_time, Unset):
            sign_up_time = UNSET
        elif isinstance(self.sign_up_time, datetime.datetime):
            sign_up_time = self.sign_up_time.isoformat()
        else:
            sign_up_time = self.sign_up_time

        last_signed_in: None | str | Unset
        if isinstance(self.last_signed_in, Unset):
            last_signed_in = UNSET
        elif isinstance(self.last_signed_in, datetime.datetime):
            last_signed_in = self.last_signed_in.isoformat()
        else:
            last_signed_in = self.last_signed_in

        groups: list[str] | None | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = self.groups

        else:
            groups = self.groups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "name": name,
                "email": email,
                "organization": organization,
                "projectAssignments": project_assignments,
                "globalRoles": global_roles,
                "settings": settings,
            }
        )
        if phone is not UNSET:
            field_dict["phone"] = phone
        if orcid_id is not UNSET:
            field_dict["orcidId"] = orcid_id
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if department is not UNSET:
            field_dict["department"] = department
        if invited_by is not UNSET:
            field_dict["invitedBy"] = invited_by
        if sign_up_time is not UNSET:
            field_dict["signUpTime"] = sign_up_time
        if last_signed_in is not UNSET:
            field_dict["lastSignedIn"] = last_signed_in
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_project_assignment import UserProjectAssignment
        from ..models.user_settings import UserSettings

        d = dict(src_dict)
        username = d.pop("username")

        name = d.pop("name")

        email = d.pop("email")

        organization = d.pop("organization")

        project_assignments = []
        _project_assignments = d.pop("projectAssignments")
        for project_assignments_item_data in _project_assignments:
            project_assignments_item = UserProjectAssignment.from_dict(project_assignments_item_data)

            project_assignments.append(project_assignments_item)

        global_roles = cast(list[str], d.pop("globalRoles"))

        settings = UserSettings.from_dict(d.pop("settings"))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_orcid_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        orcid_id = _parse_orcid_id(d.pop("orcidId", UNSET))

        def _parse_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))

        def _parse_department(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department = _parse_department(d.pop("department", UNSET))

        def _parse_invited_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invited_by = _parse_invited_by(d.pop("invitedBy", UNSET))

        def _parse_sign_up_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sign_up_time_type_0 = isoparse(data)

                return sign_up_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        sign_up_time = _parse_sign_up_time(d.pop("signUpTime", UNSET))

        def _parse_last_signed_in(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_signed_in_type_0 = isoparse(data)

                return last_signed_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_signed_in = _parse_last_signed_in(d.pop("lastSignedIn", UNSET))

        def _parse_groups(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = cast(list[str], data)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))

        user_detail = cls(
            username=username,
            name=name,
            email=email,
            organization=organization,
            project_assignments=project_assignments,
            global_roles=global_roles,
            settings=settings,
            phone=phone,
            orcid_id=orcid_id,
            job_title=job_title,
            department=department,
            invited_by=invited_by,
            sign_up_time=sign_up_time,
            last_signed_in=last_signed_in,
            groups=groups,
        )

        user_detail.additional_properties = d
        return user_detail

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
