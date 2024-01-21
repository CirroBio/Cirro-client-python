# cirro_api_client.FileApi

All URIs are relative to *https://api.cirro.bio*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_project_file_access_token**](FileApi.md#generate_project_file_access_token) | **POST** /projects/{projectId}/s3-token | Create project file access token
[**generate_project_sftp_token**](FileApi.md#generate_project_sftp_token) | **POST** /projects/{projectId}/sftp-token | Create project SFTP Token


# **generate_project_file_access_token**
> AWSCredentials generate_project_file_access_token(project_id, file_access_request)

Create project file access token

Generates credentials used for connecting via S3

### Example

* Bearer (JWT) Authentication (accessToken):

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.aws_credentials import AWSCredentials
from cirro_api_client.models.file_access_request import FileAccessRequest
from cirro_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cirro.bio
# See configuration.py for a list of all supported configuration parameters.
configuration = cirro_api_client.Configuration(
    host = "https://api.cirro.bio"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): accessToken
configuration = cirro_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cirro_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cirro_api_client.FileApi(api_client)
    project_id = 'project_id_example' # str | 
    file_access_request = cirro_api_client.FileAccessRequest() # FileAccessRequest | 

    try:
        # Create project file access token
        api_response = api_instance.generate_project_file_access_token(project_id, file_access_request)
        print("The response of FileApi->generate_project_file_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->generate_project_file_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **file_access_request** | [**FileAccessRequest**](FileAccessRequest.md)|  | 

### Return type

[**AWSCredentials**](AWSCredentials.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | generateProjectFileAccessToken 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_project_sftp_token**
> SftpCredentials generate_project_sftp_token(project_id, generate_sftp_credentials_request)

Create project SFTP Token

Generates credentials used for connecting via SFTP

### Example

* Bearer (JWT) Authentication (accessToken):

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.generate_sftp_credentials_request import GenerateSftpCredentialsRequest
from cirro_api_client.models.sftp_credentials import SftpCredentials
from cirro_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cirro.bio
# See configuration.py for a list of all supported configuration parameters.
configuration = cirro_api_client.Configuration(
    host = "https://api.cirro.bio"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): accessToken
configuration = cirro_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cirro_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cirro_api_client.FileApi(api_client)
    project_id = 'project_id_example' # str | 
    generate_sftp_credentials_request = cirro_api_client.GenerateSftpCredentialsRequest() # GenerateSftpCredentialsRequest | 

    try:
        # Create project SFTP Token
        api_response = api_instance.generate_project_sftp_token(project_id, generate_sftp_credentials_request)
        print("The response of FileApi->generate_project_sftp_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->generate_project_sftp_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **generate_sftp_credentials_request** | [**GenerateSftpCredentialsRequest**](GenerateSftpCredentialsRequest.md)|  | 

### Return type

[**SftpCredentials**](SftpCredentials.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | generateProjectSftpToken 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

