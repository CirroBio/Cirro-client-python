# DatasetDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**s3** | **str** |  | 
**process_id** | **str** |  | 
**project_id** | **str** |  | 
**source_dataset_ids** | **List[str]** |  | 
**status** | [**Status**](Status.md) |  | 
**status_message** | **str** |  | 
**tags** | [**List[Tag]**](Tag.md) |  | 
**params** | **Dict[str, object]** |  | 
**info** | **Dict[str, object]** |  | 
**created_by** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from cirro_api_client.models.dataset_detail import DatasetDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetDetail from a JSON string
dataset_detail_instance = DatasetDetail.from_json(json)
# print the JSON string representation of the object
print DatasetDetail.to_json()

# convert the object into a dict
dataset_detail_dict = dataset_detail_instance.to_dict()
# create an instance of DatasetDetail from a dict
dataset_detail_form_dict = dataset_detail.from_dict(dataset_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


