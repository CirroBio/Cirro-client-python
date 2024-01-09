# ProjectMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**costs** | [**List[MetricRecord]**](MetricRecord.md) | Costs by service by month | [optional] 
**storage_metrics** | [**List[MetricRecord]**](MetricRecord.md) | Storage usage by tier by day | [optional] 

## Example

```python
from cirro_api_client.models.project_metrics import ProjectMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMetrics from a JSON string
project_metrics_instance = ProjectMetrics.from_json(json)
# print the JSON string representation of the object
print ProjectMetrics.to_json()

# convert the object into a dict
project_metrics_dict = project_metrics_instance.to_dict()
# create an instance of ProjectMetrics from a dict
project_metrics_form_dict = project_metrics.from_dict(project_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


