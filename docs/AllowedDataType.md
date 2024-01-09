# AllowedDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**error_msg** | **str** |  | 
**allowed_patterns** | [**List[FileNamePattern]**](FileNamePattern.md) |  | 

## Example

```python
from cirro_api_client.models.allowed_data_type import AllowedDataType

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedDataType from a JSON string
allowed_data_type_instance = AllowedDataType.from_json(json)
# print the JSON string representation of the object
print AllowedDataType.to_json()

# convert the object into a dict
allowed_data_type_dict = allowed_data_type_instance.to_dict()
# create an instance of AllowedDataType from a dict
allowed_data_type_form_dict = allowed_data_type.from_dict(allowed_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


