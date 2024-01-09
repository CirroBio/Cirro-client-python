# GenerateSftpCredentialsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lifetime_days** | **int** | Number of days the credentials are valid for | [optional] [default to 1]

## Example

```python
from cirro_api_client.models.generate_sftp_credentials_request import GenerateSftpCredentialsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateSftpCredentialsRequest from a JSON string
generate_sftp_credentials_request_instance = GenerateSftpCredentialsRequest.from_json(json)
# print the JSON string representation of the object
print GenerateSftpCredentialsRequest.to_json()

# convert the object into a dict
generate_sftp_credentials_request_dict = generate_sftp_credentials_request_instance.to_dict()
# create an instance of GenerateSftpCredentialsRequest from a dict
generate_sftp_credentials_request_form_dict = generate_sftp_credentials_request.from_dict(generate_sftp_credentials_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


