# ProjectDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**billing_account_id** | **str** |  | 
**contacts** | [**List[Contact]**](Contact.md) |  | 
**status** | [**Status**](Status.md) |  | 
**settings** | [**ProjectSettings**](ProjectSettings.md) |  | 
**status_message** | **str** |  | 
**tags** | [**List[Tag]**](Tag.md) |  | 
**created_by** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from cirro_api_client.models.project_detail import ProjectDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDetail from a JSON string
project_detail_instance = ProjectDetail.from_json(json)
# print the JSON string representation of the object
print ProjectDetail.to_json()

# convert the object into a dict
project_detail_dict = project_detail_instance.to_dict()
# create an instance of ProjectDetail from a dict
project_detail_form_dict = project_detail.from_dict(project_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


