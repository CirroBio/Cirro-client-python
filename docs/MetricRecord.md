# MetricRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date in ISO 8601 format | [optional] 
**unit** | **str** |  | 
**services** | **Dict[str, float]** | Map of service names to metric value | [optional] 

## Example

```python
from cirro_api_client.models.metric_record import MetricRecord

# TODO update the JSON string below
json = "{}"
# create an instance of MetricRecord from a JSON string
metric_record_instance = MetricRecord.from_json(json)
# print the JSON string representation of the object
print MetricRecord.to_json()

# convert the object into a dict
metric_record_dict = metric_record_instance.to_dict()
# create an instance of MetricRecord from a dict
metric_record_form_dict = metric_record.from_dict(metric_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


