# cirro_api_client.DashboardsApi

All URIs are relative to *https://api.cirro.bio*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard**](DashboardsApi.md#create_dashboard) | **POST** /projects/{projectId}/dashboards | Create dashboard
[**delete_dashboard**](DashboardsApi.md#delete_dashboard) | **DELETE** /projects/{projectId}/dashboards/{dashboardId} | Delete dashboard
[**get_dashboard**](DashboardsApi.md#get_dashboard) | **GET** /projects/{projectId}/dashboards/{dashboardId} | Get dashboard
[**get_dashboards**](DashboardsApi.md#get_dashboards) | **GET** /projects/{projectId}/dashboards | List dashboards
[**update_dashboard**](DashboardsApi.md#update_dashboard) | **PUT** /projects/{projectId}/dashboards/{dashboardId} | Update dashboard


# **create_dashboard**
> CreateResponse create_dashboard(project_id, dashboard_request)

Create dashboard

Creates a dashboard

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **dashboard_request** | [**DashboardRequest**](DashboardRequest.md)|  | 

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
**200** | createDashboard 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard**
> Dashboard delete_dashboard(project_id, dashboard_id)

Delete dashboard

Deletes a dashboard

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **dashboard_id** | **str**|  | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteDashboard 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard**
> Dashboard get_dashboard(project_id, dashboard_id)

Get dashboard

Retrieves a dashboard

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **dashboard_id** | **str**|  | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getDashboard 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboards**
> List[Dashboard] get_dashboards(project_id)

List dashboards

Retrieves a list of dashboards for a given project

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**List[Dashboard]**](Dashboard.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getDashboards 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard**
> Dashboard update_dashboard(project_id, dashboard_id, dashboard_request)

Update dashboard

Updates a dashboard

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **dashboard_id** | **str**|  | 
 **dashboard_request** | [**DashboardRequest**](DashboardRequest.md)|  | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateDashboard 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

