# StopExecutionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **List[str]** | List of job IDs that were successful in termination | [optional] 
**failed** | **List[str]** | List of job IDs that were not successful in termination | [optional] 

## Example

```python
from cirro_api_client.models.stop_execution_response import StopExecutionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StopExecutionResponse from a JSON string
stop_execution_response_instance = StopExecutionResponse.from_json(json)
# print the JSON string representation of the object
print StopExecutionResponse.to_json()

# convert the object into a dict
stop_execution_response_dict = stop_execution_response_instance.to_dict()
# create an instance of StopExecutionResponse from a dict
stop_execution_response_form_dict = stop_execution_response.from_dict(stop_execution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


