# ServiceConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from cirro_api_client.models.service_connection import ServiceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConnection from a JSON string
service_connection_instance = ServiceConnection.from_json(json)
# print the JSON string representation of the object
print ServiceConnection.to_json()

# convert the object into a dict
service_connection_dict = service_connection_instance.to_dict()
# create an instance of ServiceConnection from a dict
service_connection_form_dict = service_connection.from_dict(service_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


