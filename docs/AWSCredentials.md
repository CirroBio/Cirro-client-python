# AWSCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** |  | 
**secret_access_key** | **str** |  | 
**session_token** | **str** |  | 
**expiration** | **datetime** |  | 
**region** | **str** | Region of requested resource (i.e., S3 Bucket) | [optional] 

## Example

```python
from cirro_api_client.models.aws_credentials import AWSCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of AWSCredentials from a JSON string
aws_credentials_instance = AWSCredentials.from_json(json)
# print the JSON string representation of the object
print AWSCredentials.to_json()

# convert the object into a dict
aws_credentials_dict = aws_credentials_instance.to_dict()
# create an instance of AWSCredentials from a dict
aws_credentials_form_dict = aws_credentials.from_dict(aws_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


