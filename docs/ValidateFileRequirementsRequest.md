# ValidateFileRequirementsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_sheet** | **str** |  | 
**file_names** | **List[str]** |  | 

## Example

```python
from cirro_api_client.models.validate_file_requirements_request import ValidateFileRequirementsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateFileRequirementsRequest from a JSON string
validate_file_requirements_request_instance = ValidateFileRequirementsRequest.from_json(json)
# print the JSON string representation of the object
print ValidateFileRequirementsRequest.to_json()

# convert the object into a dict
validate_file_requirements_request_dict = validate_file_requirements_request_instance.to_dict()
# create an instance of ValidateFileRequirementsRequest from a dict
validate_file_requirements_request_form_dict = validate_file_requirements_request.from_dict(validate_file_requirements_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


