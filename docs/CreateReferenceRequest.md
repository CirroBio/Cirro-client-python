# CreateReferenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**type** | **str** |  | 
**expected_files** | **List[str]** |  | 

## Example

```python
from cirro_api_client.models.create_reference_request import CreateReferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReferenceRequest from a JSON string
create_reference_request_instance = CreateReferenceRequest.from_json(json)
# print the JSON string representation of the object
print CreateReferenceRequest.to_json()

# convert the object into a dict
create_reference_request_dict = create_reference_request_instance.to_dict()
# create an instance of CreateReferenceRequest from a dict
create_reference_request_form_dict = create_reference_request.from_dict(create_reference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


