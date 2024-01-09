# CustomPipelineSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** |  | 
**branch** | **str** |  | 
**folder** | **str** |  | 
**last_sync** | **datetime** |  | 
**sync_status** | **str** |  | 
**commit_hash** | **str** |  | 

## Example

```python
from cirro_api_client.models.custom_pipeline_settings import CustomPipelineSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CustomPipelineSettings from a JSON string
custom_pipeline_settings_instance = CustomPipelineSettings.from_json(json)
# print the JSON string representation of the object
print CustomPipelineSettings.to_json()

# convert the object into a dict
custom_pipeline_settings_dict = custom_pipeline_settings_instance.to_dict()
# create an instance of CustomPipelineSettings from a dict
custom_pipeline_settings_form_dict = custom_pipeline_settings.from_dict(custom_pipeline_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


