# FileRequirements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **List[str]** |  | 
**error_msg** | **str** |  | 
**allowed_data_types** | [**List[AllowedDataType]**](AllowedDataType.md) |  | 

## Example

```python
from cirro_api_client.models.file_requirements import FileRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of FileRequirements from a JSON string
file_requirements_instance = FileRequirements.from_json(json)
# print the JSON string representation of the object
print FileRequirements.to_json()

# convert the object into a dict
file_requirements_dict = file_requirements_instance.to_dict()
# create an instance of FileRequirements from a dict
file_requirements_form_dict = file_requirements.from_dict(file_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


