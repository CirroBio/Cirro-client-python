# BillingAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**organization** | **str** |  | 
**contacts** | [**List[Contact]**](Contact.md) |  | 
**customer_type** | [**CustomerType**](CustomerType.md) |  | 
**billing_method** | [**BillingMethod**](BillingMethod.md) |  | 
**primary_budget_number** | **str** |  | 
**owner** | **str** |  | 
**shared_with** | **List[str]** |  | 
**is_archived** | **bool** |  | 

## Example

```python
from cirro_api_client.models.billing_account import BillingAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BillingAccount from a JSON string
billing_account_instance = BillingAccount.from_json(json)
# print the JSON string representation of the object
print BillingAccount.to_json()

# convert the object into a dict
billing_account_dict = billing_account_instance.to_dict()
# create an instance of BillingAccount from a dict
billing_account_form_dict = billing_account.from_dict(billing_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


