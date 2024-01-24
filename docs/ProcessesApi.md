# cirro_api_client.ProcessesApi

All URIs are relative to *https://api.cirro.bio*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_custom_process**](ProcessesApi.md#archive_custom_process) | **DELETE** /processes/{processId} | Archive custom process
[**create_custom_process**](ProcessesApi.md#create_custom_process) | **POST** /processes | Create custom process
[**get_process**](ProcessesApi.md#get_process) | **GET** /processes/{processId} | Get process
[**get_process_parameters**](ProcessesApi.md#get_process_parameters) | **GET** /processes/{processId}/parameters | Get process parameters
[**get_processes**](ProcessesApi.md#get_processes) | **GET** /processes | List processes
[**sync_custom_process**](ProcessesApi.md#sync_custom_process) | **PUT** /processes/{processId}:sync | Sync custom process
[**update_custom_process**](ProcessesApi.md#update_custom_process) | **PUT** /processes/{processId} | Update custom process
[**validate_file_requirements**](ProcessesApi.md#validate_file_requirements) | **POST** /processes/{processId}/validate-files | Validate file requirements


# **archive_custom_process**
> archive_custom_process(process_id)

Archive custom process

Removes the process from the list of available options

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | archiveCustomProcess 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_process**
> CreateResponse create_custom_process(process_detail)

Create custom process

Creates a custom data type or pipeline which you can use in the listed projects.

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_detail** | [**ProcessDetail**](ProcessDetail.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**200** | createCustomProcess 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process**
> ProcessDetail get_process(process_id)

Get process

Retrieves detailed information on a process

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**|  | 

### Return type

[**ProcessDetail**](ProcessDetail.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getProcess 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_parameters**
> FormSchema get_process_parameters(process_id)

Get process parameters

Retrieves the input parameters for a process

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**|  | 

### Return type

[**FormSchema**](FormSchema.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getProcessParameters 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_processes**
> List[Process] get_processes(include_archived=include_archived)

List processes

Retrieves a list of available processes

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_archived** | **bool**| Include processes that are no longer in use | [optional] [default to False]

### Return type

[**List[Process]**](Process.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list is successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_custom_process**
> CustomPipelineSettings sync_custom_process(process_id)

Sync custom process

Updates the process definition from the repository

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**|  | 

### Return type

[**CustomPipelineSettings**](CustomPipelineSettings.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | syncCustomProcess 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_process**
> update_custom_process(process_id, process_detail)

Update custom process

Updates the custom process

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**|  | 
 **process_detail** | [**ProcessDetail**](ProcessDetail.md)|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateCustomProcess 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_file_requirements**
> FileRequirements validate_file_requirements(process_id, validate_file_requirements_request)

Validate file requirements

Checks the input file names with the expected files for a data type (ingest processes only)

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**|  | 
 **validate_file_requirements_request** | [**ValidateFileRequirementsRequest**](ValidateFileRequirementsRequest.md)|  | 

### Return type

[**FileRequirements**](FileRequirements.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | validateFileRequirements 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

