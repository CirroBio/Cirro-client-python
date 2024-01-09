# CreateNotebookInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**instance_type** | **str** | AWS EC2 Instance Type (see list of available options) | 
**accelerator_types** | **List[str]** |  | 
**volume_size_gb** | **int** |  | 

## Example

```python
from cirro_api_client.models.create_notebook_instance_request import CreateNotebookInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotebookInstanceRequest from a JSON string
create_notebook_instance_request_instance = CreateNotebookInstanceRequest.from_json(json)
# print the JSON string representation of the object
print CreateNotebookInstanceRequest.to_json()

# convert the object into a dict
create_notebook_instance_request_dict = create_notebook_instance_request_instance.to_dict()
# create an instance of CreateNotebookInstanceRequest from a dict
create_notebook_instance_request_form_dict = create_notebook_instance_request.from_dict(create_notebook_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


