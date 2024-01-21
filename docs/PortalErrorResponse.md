# PortalErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | 
**error_code** | **str** |  | 
**error_detail** | **str** |  | 
**errors** | [**List[ErrorMessage]**](ErrorMessage.md) |  | 

## Example

```python
from cirro_api_client.models.portal_error_response import PortalErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PortalErrorResponse from a JSON string
portal_error_response_instance = PortalErrorResponse.from_json(json)
# print the JSON string representation of the object
print PortalErrorResponse.to_json()

# convert the object into a dict
portal_error_response_dict = portal_error_response_instance.to_dict()
# create an instance of PortalErrorResponse from a dict
portal_error_response_form_dict = portal_error_response.from_dict(portal_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


