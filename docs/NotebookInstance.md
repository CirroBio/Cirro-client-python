# NotebookInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**status** | [**Status**](Status.md) |  | 
**instance_type** | **str** |  | 
**accelerator_types** | **List[str]** |  | 
**volume_size_gb** | **int** |  | 
**created_by** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from cirro_api_client.models.notebook_instance import NotebookInstance

# TODO update the JSON string below
json = "{}"
# create an instance of NotebookInstance from a JSON string
notebook_instance_instance = NotebookInstance.from_json(json)
# print the JSON string representation of the object
print NotebookInstance.to_json()

# convert the object into a dict
notebook_instance_dict = notebook_instance_instance.to_dict()
# create an instance of NotebookInstance from a dict
notebook_instance_form_dict = notebook_instance.from_dict(notebook_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


