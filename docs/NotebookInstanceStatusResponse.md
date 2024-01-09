# NotebookInstanceStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**status_message** | **str** |  | 

## Example

```python
from cirro_api_client.models.notebook_instance_status_response import NotebookInstanceStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotebookInstanceStatusResponse from a JSON string
notebook_instance_status_response_instance = NotebookInstanceStatusResponse.from_json(json)
# print the JSON string representation of the object
print NotebookInstanceStatusResponse.to_json()

# convert the object into a dict
notebook_instance_status_response_dict = notebook_instance_status_response_instance.to_dict()
# create an instance of NotebookInstanceStatusResponse from a dict
notebook_instance_status_response_form_dict = notebook_instance_status_response.from_dict(notebook_instance_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


