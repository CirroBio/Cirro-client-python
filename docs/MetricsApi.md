# cirro_api_client.MetricsApi

All URIs are relative to *https://api.cirro.bio*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_metrics**](MetricsApi.md#get_all_metrics) | **GET** /metrics | Get all project metrics
[**get_project_metrics**](MetricsApi.md#get_project_metrics) | **GET** /projects/{projectId}/metrics | Get project metrics


# **get_all_metrics**
> List[ProjectMetrics] get_all_metrics()

Get all project metrics

Retrieves metrics for all projects.

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ProjectMetrics]**](ProjectMetrics.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getAllMetrics 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_metrics**
> ProjectMetrics get_project_metrics(project_id)

Get project metrics

Retrieves metrics about a project.

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**ProjectMetrics**](ProjectMetrics.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getProjectMetrics 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

