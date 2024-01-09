# DashboardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**process_ids** | **List[str]** |  | 
**dashboard_data** | **Dict[str, object]** |  | 
**info** | **Dict[str, object]** |  | 

## Example

```python
from cirro_api_client.models.dashboard_request import DashboardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardRequest from a JSON string
dashboard_request_instance = DashboardRequest.from_json(json)
# print the JSON string representation of the object
print DashboardRequest.to_json()

# convert the object into a dict
dashboard_request_dict = dashboard_request_instance.to_dict()
# create an instance of DashboardRequest from a dict
dashboard_request_form_dict = dashboard_request.from_dict(dashboard_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


