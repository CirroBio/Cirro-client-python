# UpdateDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**process_id** | **str** |  | 
**tags** | [**List[Tag]**](Tag.md) |  | 

## Example

```python
from cirro_api_client.models.update_dataset_request import UpdateDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDatasetRequest from a JSON string
update_dataset_request_instance = UpdateDatasetRequest.from_json(json)
# print the JSON string representation of the object
print UpdateDatasetRequest.to_json()

# convert the object into a dict
update_dataset_request_dict = update_dataset_request_instance.to_dict()
# create an instance of UpdateDatasetRequest from a dict
update_dataset_request_form_dict = update_dataset_request.from_dict(update_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


