# SampleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**metadata** | **Dict[str, object]** |  | 

## Example

```python
from cirro_api_client.models.sample_request import SampleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SampleRequest from a JSON string
sample_request_instance = SampleRequest.from_json(json)
# print the JSON string representation of the object
print SampleRequest.to_json()

# convert the object into a dict
sample_request_dict = sample_request_instance.to_dict()
# create an instance of SampleRequest from a dict
sample_request_form_dict = sample_request.from_dict(sample_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


