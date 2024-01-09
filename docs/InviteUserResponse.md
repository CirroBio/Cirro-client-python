# InviteUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from cirro_api_client.models.invite_user_response import InviteUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InviteUserResponse from a JSON string
invite_user_response_instance = InviteUserResponse.from_json(json)
# print the JSON string representation of the object
print InviteUserResponse.to_json()

# convert the object into a dict
invite_user_response_dict = invite_user_response_instance.to_dict()
# create an instance of InviteUserResponse from a dict
invite_user_response_form_dict = invite_user_response.from_dict(invite_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


