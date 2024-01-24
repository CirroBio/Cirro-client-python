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

