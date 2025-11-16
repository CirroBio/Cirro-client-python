from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FulfillmentResponse")


@_attrs_define
class FulfillmentResponse:
    """
    Attributes:
        fulfillment_id (str):
        path (str):
    """

    fulfillment_id: str
    path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fulfillment_id = self.fulfillment_id

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fulfillmentId": fulfillment_id,
                "path": path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        fulfillment_id = d.pop("fulfillmentId")

        path = d.pop("path")

        fulfillment_response = cls(
            fulfillment_id=fulfillment_id,
            path=path,
        )

        fulfillment_response.additional_properties = d
        return fulfillment_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())
