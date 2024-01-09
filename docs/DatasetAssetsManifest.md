# DatasetAssetsManifest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Base URL for files | [optional] 
**files** | [**List[DatasetFile]**](DatasetFile.md) | List of files in the dataset, including metadata | [optional] 
**viz** | [**List[DatasetViz]**](DatasetViz.md) | List of viz to render for the dataset | [optional] 

## Example

```python
from cirro_api_client.models.dataset_assets_manifest import DatasetAssetsManifest

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetAssetsManifest from a JSON string
dataset_assets_manifest_instance = DatasetAssetsManifest.from_json(json)
# print the JSON string representation of the object
print DatasetAssetsManifest.to_json()

# convert the object into a dict
dataset_assets_manifest_dict = dataset_assets_manifest_instance.to_dict()
# create an instance of DatasetAssetsManifest from a dict
dataset_assets_manifest_form_dict = dataset_assets_manifest.from_dict(dataset_assets_manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


