# SystemInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sdk_app_id** | **str** |  | 
**resources_bucket** | **str** |  | 
**data_endpoint** | **str** |  | 
**region** | **str** |  | 
**system_message** | **str** |  | 
**commit_hash** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from cirro_api_client.models.system_info_response import SystemInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SystemInfoResponse from a JSON string
system_info_response_instance = SystemInfoResponse.from_json(json)
# print the JSON string representation of the object
print SystemInfoResponse.to_json()

# convert the object into a dict
system_info_response_dict = system_info_response_instance.to_dict()
# create an instance of SystemInfoResponse from a dict
system_info_response_form_dict = system_info_response.from_dict(system_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


