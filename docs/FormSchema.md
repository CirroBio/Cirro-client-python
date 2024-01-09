# FormSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form** | **Dict[str, object]** | JSONSchema representation of the parameters | [optional] 
**ui** | **Dict[str, object]** | Describes how the form should be rendered, see rjsf | [optional] 

## Example

```python
from cirro_api_client.models.form_schema import FormSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FormSchema from a JSON string
form_schema_instance = FormSchema.from_json(json)
# print the JSON string representation of the object
print FormSchema.to_json()

# convert the object into a dict
form_schema_dict = form_schema_instance.to_dict()
# create an instance of FormSchema from a dict
form_schema_form_dict = form_schema.from_dict(form_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


