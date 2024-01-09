# BillingAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**contacts** | [**List[Contact]**](Contact.md) |  | 
**customer_type** | [**CustomerType**](CustomerType.md) |  | 
**billing_method** | [**BillingMethod**](BillingMethod.md) |  | 
**primary_budget_number** | **str** |  | 
**owner** | **str** |  | 
**shared_with** | **List[str]** |  | 

## Example

```python
from cirro_api_client.models.billing_account_request import BillingAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BillingAccountRequest from a JSON string
billing_account_request_instance = BillingAccountRequest.from_json(json)
# print the JSON string representation of the object
print BillingAccountRequest.to_json()

# convert the object into a dict
billing_account_request_dict = billing_account_request_instance.to_dict()
# create an instance of BillingAccountRequest from a dict
billing_account_request_form_dict = billing_account_request.from_dict(billing_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


