from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cloud_account_type import CloudAccountType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudAccount")


@_attrs_define
class CloudAccount:
    """
    Attributes:
        account_id (str): AWS Account ID
        region_name (str): AWS Region Code Example: us-west-2.
        account_type (CloudAccountType): Type of cloud account (Hosted by Cirro, or Bring your own account)
        account_name (Union[Unset, str]): Name used to describe the account, useful when the account hosts multiple
            projects
    """

    account_id: str
    region_name: str
    account_type: CloudAccountType
    account_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id

        region_name = self.region_name

        account_type = self.account_type.value

        account_name = self.account_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "regionName": region_name,
                "accountType": account_type,
            }
        )
        if account_name is not UNSET:
            field_dict["accountName"] = account_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId")

        region_name = d.pop("regionName")

        account_type = CloudAccountType(d.pop("accountType"))

        account_name = d.pop("accountName", UNSET)

        cloud_account = cls(
            account_id=account_id,
            region_name=region_name,
            account_type=account_type,
            account_name=account_name,
        )

        cloud_account.additional_properties = d
        return cloud_account

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())
