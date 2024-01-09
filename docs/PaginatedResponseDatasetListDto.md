# PaginatedResponseDatasetListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Dataset]**](Dataset.md) |  | 
**next_token** | **str** |  | 

## Example

```python
from cirro_api_client.models.paginated_response_dataset_list_dto import PaginatedResponseDatasetListDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseDatasetListDto from a JSON string
paginated_response_dataset_list_dto_instance = PaginatedResponseDatasetListDto.from_json(json)
# print the JSON string representation of the object
print PaginatedResponseDatasetListDto.to_json()

# convert the object into a dict
paginated_response_dataset_list_dto_dict = paginated_response_dataset_list_dto_instance.to_dict()
# create an instance of PaginatedResponseDatasetListDto from a dict
paginated_response_dataset_list_dto_form_dict = paginated_response_dataset_list_dto.from_dict(paginated_response_dataset_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


