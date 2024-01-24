# Process


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the Process | 
**name** | **str** | Friendly name for the process | [optional] 
**description** | **str** |  | [optional] 
**executor** | [**Executor**](Executor.md) |  | 
**documentation_url** | **str** | Link to pipeline documentation | [optional] 
**file_requirements_message** | **str** | Description of the files to be uploaded (optional) | [optional] 
**child_process_ids** | **List[str]** | IDs of pipelines that can be ran downstream | [optional] 
**parent_process_ids** | **List[str]** | IDs of pipelines that can run this pipeline | [optional] 
**owner** | **str** | Username of the pipeline creator (blank if Cirro curated) | [optional] 
**linked_project_ids** | **List[str]** | Projects that can run this pipeline | [optional] 

## Example

```python
from cirro_api_client.models.process import Process

# TODO update the JSON string below
json = "{}"
# create an instance of Process from a JSON string
process_instance = Process.from_json(json)
# print the JSON string representation of the object
print Process.to_json()

# convert the object into a dict
process_dict = process_instance.to_dict()
# create an instance of Process from a dict
process_form_dict = process.from_dict(process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


