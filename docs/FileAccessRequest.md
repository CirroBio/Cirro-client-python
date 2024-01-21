# FileAccessRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | [**AccessType**](AccessType.md) |  | 
**dataset_id** | **str** |  | [optional] 
**token_lifetime_hours** | **int** |  | [optional] 

## Example

```python
from cirro_api_client.models.file_access_request import FileAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileAccessRequest from a JSON string
file_access_request_instance = FileAccessRequest.from_json(json)
# print the JSON string representation of the object
print FileAccessRequest.to_json()

# convert the object into a dict
file_access_request_dict = file_access_request_instance.to_dict()
# create an instance of FileAccessRequest from a dict
file_access_request_form_dict = file_access_request.from_dict(file_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


