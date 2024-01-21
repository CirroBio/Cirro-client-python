# ProcessDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**executor** | [**Executor**](Executor.md) |  | 
**documentation_url** | **str** |  | [optional] 
**file_requirements_message** | **str** |  | [optional] 
**child_process_ids** | **List[str]** |  | 
**parent_process_ids** | **List[str]** |  | 
**owner** | **str** |  | [optional] 
**linked_project_ids** | **List[str]** |  | 
**pipeline_code** | [**ProcessDetailAllOfPipelineCode**](ProcessDetailAllOfPipelineCode.md) |  | [optional] 
**custom_settings** | [**CustomPipelineSettings**](CustomPipelineSettings.md) |  | 
**is_archived** | **bool** | Whether the process is marked for removal | [optional] 

## Example

```python
from cirro_api_client.models.process_detail import ProcessDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessDetail from a JSON string
process_detail_instance = ProcessDetail.from_json(json)
# print the JSON string representation of the object
print ProcessDetail.to_json()

# convert the object into a dict
process_detail_dict = process_detail_instance.to_dict()
# create an instance of ProcessDetail from a dict
process_detail_form_dict = process_detail.from_dict(process_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


