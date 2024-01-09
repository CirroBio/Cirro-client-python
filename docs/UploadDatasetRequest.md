# UploadDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**process_id** | **str** |  | 
**expected_files** | **List[str]** |  | 

## Example

```python
from cirro_api_client.models.upload_dataset_request import UploadDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadDatasetRequest from a JSON string
upload_dataset_request_instance = UploadDatasetRequest.from_json(json)
# print the JSON string representation of the object
print UploadDatasetRequest.to_json()

# convert the object into a dict
upload_dataset_request_dict = upload_dataset_request_instance.to_dict()
# create an instance of UploadDatasetRequest from a dict
upload_dataset_request_form_dict = upload_dataset_request.from_dict(upload_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


