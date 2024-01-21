# ProcessDetailAllOfPipelineCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_path** | **str** | GitHub repository which contains the workflow code | 
**version** | **str** | Branch, tag, or commit hash of the pipeline code | 
**repository_type** | [**RepositoryType**](RepositoryType.md) |  | [optional] 
**entry_point** | **str** | Main script for running the pipeline | 

## Example

```python
from cirro_api_client.models.process_detail_all_of_pipeline_code import ProcessDetailAllOfPipelineCode

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessDetailAllOfPipelineCode from a JSON string
process_detail_all_of_pipeline_code_instance = ProcessDetailAllOfPipelineCode.from_json(json)
# print the JSON string representation of the object
print ProcessDetailAllOfPipelineCode.to_json()

# convert the object into a dict
process_detail_all_of_pipeline_code_dict = process_detail_all_of_pipeline_code_instance.to_dict()
# create an instance of ProcessDetailAllOfPipelineCode from a dict
process_detail_all_of_pipeline_code_form_dict = process_detail_all_of_pipeline_code.from_dict(process_detail_all_of_pipeline_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


