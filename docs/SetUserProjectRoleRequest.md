# SetUserProjectRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**role** | [**ProjectRole**](ProjectRole.md) |  | 
**supress_notification** | **bool** |  | [optional] [default to False]

## Example

```python
from cirro_api_client.models.set_user_project_role_request import SetUserProjectRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetUserProjectRoleRequest from a JSON string
set_user_project_role_request_instance = SetUserProjectRoleRequest.from_json(json)
# print the JSON string representation of the object
print SetUserProjectRoleRequest.to_json()

# convert the object into a dict
set_user_project_role_request_dict = set_user_project_role_request_instance.to_dict()
# create an instance of SetUserProjectRoleRequest from a dict
set_user_project_role_request_form_dict = set_user_project_role_request.from_dict(set_user_project_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


