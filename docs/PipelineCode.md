# PipelineCode

Used to describe the pipeline analysis code, not required for ingest processes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_path** | **str** | GitHub repository which contains the workflow code | 
**version** | **str** | Branch, tag, or commit hash of the pipeline code | 
**repository_type** | [**RepositoryType**](RepositoryType.md) |  | [optional] 
**entry_point** | **str** | Main script for running the pipeline | 

## Example

```python
from cirro_api_client.models.pipeline_code import PipelineCode

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineCode from a JSON string
pipeline_code_instance = PipelineCode.from_json(json)
# print the JSON string representation of the object
print PipelineCode.to_json()

# convert the object into a dict
pipeline_code_dict = pipeline_code_instance.to_dict()
# create an instance of PipelineCode from a dict
pipeline_code_form_dict = pipeline_code.from_dict(pipeline_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


