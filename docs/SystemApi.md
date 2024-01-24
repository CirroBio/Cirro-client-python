# cirro_api_client.SystemApi

All URIs are relative to *https://api.cirro.bio*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_connections**](SystemApi.md#get_service_connections) | **GET** /service-connections | Get service connections
[**info**](SystemApi.md#info) | **GET** /info | Get system info


# **get_service_connections**
> List[ServiceConnection] get_service_connections()

Get service connections

List available service connections

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ServiceConnection]**](ServiceConnection.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getServiceConnections 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info**
> SystemInfoResponse info()

Get system info

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemInfoResponse**](SystemInfoResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | info 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

