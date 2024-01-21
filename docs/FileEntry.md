# FileEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Relative path to file | [optional] 
**size** | **int** | File size (in bytes) | [optional] 
**metadata** | **Dict[str, str]** | Metadata associated with the file | [optional] 

## Example

```python
from cirro_api_client.models.file_entry import FileEntry

# TODO update the JSON string below
json = "{}"
# create an instance of FileEntry from a JSON string
file_entry_instance = FileEntry.from_json(json)
# print the JSON string representation of the object
print FileEntry.to_json()

# convert the object into a dict
file_entry_dict = file_entry_instance.to_dict()
# create an instance of FileEntry from a dict
file_entry_form_dict = file_entry.from_dict(file_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


