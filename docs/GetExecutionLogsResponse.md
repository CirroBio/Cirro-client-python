# GetExecutionLogsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[LogEntry]**](LogEntry.md) |  | 

## Example

```python
from cirro_api_client.models.get_execution_logs_response import GetExecutionLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetExecutionLogsResponse from a JSON string
get_execution_logs_response_instance = GetExecutionLogsResponse.from_json(json)
# print the JSON string representation of the object
print GetExecutionLogsResponse.to_json()

# convert the object into a dict
get_execution_logs_response_dict = get_execution_logs_response_instance.to_dict()
# create an instance of GetExecutionLogsResponse from a dict
get_execution_logs_response_form_dict = get_execution_logs_response.from_dict(get_execution_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


