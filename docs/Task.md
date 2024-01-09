# Task


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**native_job_id** | **str** |  | 
**status** | **str** |  | 
**requested_at** | **datetime** |  | 
**stopped_at** | **datetime** |  | [optional] 
**container_image** | **str** |  | [optional] 
**command_line** | **str** |  | [optional] 
**log_location** | **str** |  | [optional] 

## Example

```python
from cirro_api_client.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print Task.to_json()

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_form_dict = task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


