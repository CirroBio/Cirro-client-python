# DatasetViz


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of viz | [optional] 
**desc** | **str** | Description of viz | [optional] 
**type** | **str** | Type of viz | [optional] 
**config** | **str** | Path to config file used to render viz | [optional] 

## Example

```python
from cirro_api_client.models.dataset_viz import DatasetViz

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetViz from a JSON string
dataset_viz_instance = DatasetViz.from_json(json)
# print the JSON string representation of the object
print DatasetViz.to_json()

# convert the object into a dict
dataset_viz_dict = dataset_viz_instance.to_dict()
# create an instance of DatasetViz from a dict
dataset_viz_form_dict = dataset_viz.from_dict(dataset_viz_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


