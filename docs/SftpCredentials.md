# SftpCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 
**project_id** | **str** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from cirro_api_client.models.sftp_credentials import SftpCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of SftpCredentials from a JSON string
sftp_credentials_instance = SftpCredentials.from_json(json)
# print the JSON string representation of the object
print SftpCredentials.to_json()

# convert the object into a dict
sftp_credentials_dict = sftp_credentials_instance.to_dict()
# create an instance of SftpCredentials from a dict
sftp_credentials_form_dict = sftp_credentials.from_dict(sftp_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


