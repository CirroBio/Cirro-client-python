# cirro_api_client.MetadataApi

All URIs are relative to *https://api.cirro.bio*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_project_samples**](MetadataApi.md#get_project_samples) | **GET** /projects/{projectId}/samples | Get project samples
[**get_project_schema**](MetadataApi.md#get_project_schema) | **GET** /projects/{projectId}/schema | Get project metadata schema
[**update_project_schema**](MetadataApi.md#update_project_schema) | **PUT** /projects/{projectId}/schema | Update project metadata schema
[**update_sample**](MetadataApi.md#update_sample) | **PUT** /projects/{projectId}/samples/{sampleId} | Update sample


# **get_project_samples**
> PaginatedResponseSampleDto get_project_samples(project_id, limit=limit, next_token=next_token)

Get project samples

Retrieves a list of samples associated with a project along with their metadata

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **limit** | **int**| number of records to get | [optional] [default to 10000]
 **next_token** | **str**| cursor to request the next page | [optional] 

### Return type

[**PaginatedResponseSampleDto**](PaginatedResponseSampleDto.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getProjectSamples 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_schema**
> FormSchema get_project_schema(project_id)

Get project metadata schema

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

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
**200** | getProjectSchema 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_schema**
> update_project_schema(project_id, form_schema)

Update project metadata schema

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **form_schema** | [**FormSchema**](FormSchema.md)|  | 

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
**200** | updateProjectSchema 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sample**
> Sample update_sample(project_id, sample_id, sample_request)

Update sample

Updates metadata on a sample

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sample_id** | **str**|  | 
 **sample_request** | [**SampleRequest**](SampleRequest.md)|  | 

### Return type

[**Sample**](Sample.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateSample 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

