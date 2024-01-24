# cirro_api_client.NotebooksApi

All URIs are relative to *https://api.cirro.bio*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notebook_instance**](NotebooksApi.md#create_notebook_instance) | **POST** /projects/{projectId}/notebook-instances | Create notebook instance
[**delete_notebook_instance**](NotebooksApi.md#delete_notebook_instance) | **DELETE** /projects/{projectId}/notebook-instances/{notebookInstanceId} | Delete notebook instance
[**generate_notebook_instance_url**](NotebooksApi.md#generate_notebook_instance_url) | **GET** /projects/{projectId}/notebook-instances/{notebookInstanceId}:generate-url | Generate notebook instance URL
[**get_notebook_instance_status**](NotebooksApi.md#get_notebook_instance_status) | **GET** /projects/{projectId}/notebook-instances/{notebookInstanceId}:status | Get notebook instance status
[**get_notebook_instances**](NotebooksApi.md#get_notebook_instances) | **GET** /projects/{projectId}/notebook-instances | Get notebook instances
[**stop_notebook_instance**](NotebooksApi.md#stop_notebook_instance) | **POST** /projects/{projectId}/notebook-instances/{notebookInstanceId}:stop | Stop notebook instance


# **create_notebook_instance**
> CreateResponse create_notebook_instance(project_id, create_notebook_instance_request)

Create notebook instance

Creates a notebook instance within the project

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_notebook_instance_request** | [**CreateNotebookInstanceRequest**](CreateNotebookInstanceRequest.md)|  | 

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
**200** | createNotebookInstance 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notebook_instance**
> delete_notebook_instance(notebook_instance_id, project_id)

Delete notebook instance

Triggers a deletion of the notebook instance

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notebook_instance_id** | **str**|  | 
 **project_id** | **str**|  | 

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
**200** | deleteNotebookInstance 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_notebook_instance_url**
> OpenNotebookInstanceResponse generate_notebook_instance_url(notebook_instance_id, project_id)

Generate notebook instance URL

Creates an authenticated URL to open up the notebook instance in your browser

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notebook_instance_id** | **str**|  | 
 **project_id** | **str**|  | 

### Return type

[**OpenNotebookInstanceResponse**](OpenNotebookInstanceResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | generateNotebookInstanceUrl 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notebook_instance_status**
> NotebookInstanceStatusResponse get_notebook_instance_status(notebook_instance_id, project_id)

Get notebook instance status

Retrieves the status of the instance

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notebook_instance_id** | **str**|  | 
 **project_id** | **str**|  | 

### Return type

[**NotebookInstanceStatusResponse**](NotebookInstanceStatusResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getNotebookInstanceStatus 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notebook_instances**
> List[NotebookInstance] get_notebook_instances(project_id)

Get notebook instances

Retrieves a list of notebook instances that the user has access to

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**List[NotebookInstance]**](NotebookInstance.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getNotebookInstances 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_notebook_instance**
> stop_notebook_instance(notebook_instance_id, project_id)

Stop notebook instance

Shuts down a running notebook instance

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notebook_instance_id** | **str**|  | 
 **project_id** | **str**|  | 

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
**200** | stopNotebookInstance 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

