import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_event_changes import AuditEventChanges
    from ..models.audit_event_event_detail import AuditEventEventDetail


T = TypeVar("T", bound="AuditEvent")


@_attrs_define
class AuditEvent:
    """
    Attributes:
        id (Union[Unset, str]): The unique identifier for the audit event
        event_type (Union[Unset, str]): The type of event Example: CREATE.
        project_id (Union[Unset, str]): The project ID associated with the event (if applicable)
        entity_id (Union[Unset, str]): The entity ID associated with the event
        entity_type (Union[Unset, str]): The entity type associated with the event Example: Project.
        event_detail (Union['AuditEventEventDetailType0', None, Unset]): The details of the event, such as the request
            details sent from the client
        changes (Union['AuditEventChangesType0', None, Unset]): The changes made to the entity (if applicable) Example:
            {'.settings.retentionPolicyDays': '1 -> 2'}.
        username (Union[Unset, str]): The username of the user who performed the action Example: admin@cirro.bio.
        ip_address (Union[Unset, str]): The IP address of the user who performed the action Example: 0.0.0.0.
        created_at (Union[Unset, datetime.datetime]): The date and time the event was created
    """

    id: Union[Unset, str] = UNSET
    event_type: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    entity_id: Union[Unset, str] = UNSET
    entity_type: Union[Unset, str] = UNSET
    event_detail: Union[Unset, "AuditEventEventDetail"] = UNSET
    changes: Union[Unset, "AuditEventChanges"] = UNSET
    username: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        event_type = self.event_type

        project_id = self.project_id

        entity_id = self.entity_id

        entity_type = self.entity_type

        event_detail: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.event_detail, Unset):
            event_detail = self.event_detail.to_dict()

        changes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.changes, Unset):
            changes = self.changes.to_dict()

        username = self.username

        ip_address = self.ip_address

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if event_detail is not UNSET:
            field_dict["eventDetail"] = event_detail
        if changes is not UNSET:
            field_dict["changes"] = changes
        if username is not UNSET:
            field_dict["username"] = username
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.audit_event_changes import AuditEventChanges
        from ..models.audit_event_event_detail import AuditEventEventDetail

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        event_type = d.pop("eventType", UNSET)

        project_id = d.pop("projectId", UNSET)

        entity_id = d.pop("entityId", UNSET)

        entity_type = d.pop("entityType", UNSET)

        _event_detail = d.pop("eventDetail", UNSET)
        event_detail: Union[Unset, AuditEventEventDetail]
        if isinstance(_event_detail, Unset):
            event_detail = UNSET
        else:
            event_detail = AuditEventEventDetail.from_dict(_event_detail)

        _changes = d.pop("changes", UNSET)
        changes: Union[Unset, AuditEventChanges]
        if isinstance(_changes, Unset):
            changes = UNSET
        else:
            changes = AuditEventChanges.from_dict(_changes)

        username = d.pop("username", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        audit_event = cls(
            id=id,
            event_type=event_type,
            project_id=project_id,
            entity_id=entity_id,
            entity_type=entity_type,
            event_detail=event_detail,
            changes=changes,
            username=username,
            ip_address=ip_address,
            created_at=created_at,
        )

        audit_event.additional_properties = d
        return audit_event

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())
