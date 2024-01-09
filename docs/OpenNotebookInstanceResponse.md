# OpenNotebookInstanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from cirro_api_client.models.open_notebook_instance_response import OpenNotebookInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OpenNotebookInstanceResponse from a JSON string
open_notebook_instance_response_instance = OpenNotebookInstanceResponse.from_json(json)
# print the JSON string representation of the object
print OpenNotebookInstanceResponse.to_json()

# convert the object into a dict
open_notebook_instance_response_dict = open_notebook_instance_response_instance.to_dict()
# create an instance of OpenNotebookInstanceResponse from a dict
open_notebook_instance_response_form_dict = open_notebook_instance_response.from_dict(open_notebook_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


