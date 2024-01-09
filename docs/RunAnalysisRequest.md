# RunAnalysisRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**process_id** | **str** |  | 
**source_dataset_ids** | **List[str]** |  | 
**resume_dataset_id** | **str** |  | 
**params** | **Dict[str, object]** |  | 
**notification_emails** | **List[str]** |  | 

## Example

```python
from cirro_api_client.models.run_analysis_request import RunAnalysisRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunAnalysisRequest from a JSON string
run_analysis_request_instance = RunAnalysisRequest.from_json(json)
# print the JSON string representation of the object
print RunAnalysisRequest.to_json()

# convert the object into a dict
run_analysis_request_dict = run_analysis_request_instance.to_dict()
# create an instance of RunAnalysisRequest from a dict
run_analysis_request_form_dict = run_analysis_request.from_dict(run_analysis_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


