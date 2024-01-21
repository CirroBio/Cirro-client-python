# ResourcesInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit** | **str** |  | 
**var_date** | **datetime** |  | 
**repository** | **str** |  | 
**source_version** | **str** |  | 

## Example

```python
from cirro_api_client.models.resources_info import ResourcesInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesInfo from a JSON string
resources_info_instance = ResourcesInfo.from_json(json)
# print the JSON string representation of the object
print ResourcesInfo.to_json()

# convert the object into a dict
resources_info_dict = resources_info_instance.to_dict()
# create an instance of ResourcesInfo from a dict
resources_info_form_dict = resources_info.from_dict(resources_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


