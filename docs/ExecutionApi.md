# cirro_api_client.ExecutionApi

All URIs are relative to *https://api.cirro.bio*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_execution_logs**](ExecutionApi.md#get_execution_logs) | **GET** /projects/{projectId}/execution/{datasetId}/logs | Get execution logs
[**get_project_summary**](ExecutionApi.md#get_project_summary) | **GET** /projects/{projectId}/execution | Get execution summary
[**get_task_logs**](ExecutionApi.md#get_task_logs) | **GET** /projects/{projectId}/execution/{datasetId}/tasks/{taskId}/logs | Get task logs
[**get_tasks_for_execution**](ExecutionApi.md#get_tasks_for_execution) | **GET** /projects/{projectId}/execution/{datasetId}/tasks | Get execution tasks
[**run_analysis**](ExecutionApi.md#run_analysis) | **POST** /projects/{projectId}/execution | Run analysis
[**stop_analysis**](ExecutionApi.md#stop_analysis) | **PUT** /projects/{projectId}/execution/{datasetId}/stop | Stop execution


# **get_execution_logs**
> GetExecutionLogsResponse get_execution_logs(dataset_id, project_id, force_live=force_live)

Get execution logs

Gets live logs from main execution task

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **project_id** | **str**|  | 
 **force_live** | **bool**| force retrieving this info from the executor | [optional] [default to False]

### Return type

[**GetExecutionLogsResponse**](GetExecutionLogsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getExecutionLogs 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_summary**
> Dict[str, List[Task]] get_project_summary(project_id, number_of_days=number_of_days)

Get execution summary

Gets an overview of the executions currently running in the project

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **number_of_days** | **int**| Number of days of job history to pull | [optional] [default to 1]

### Return type

**Dict[str, List[Task]]**

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object with keys as the job queue name, and a list of jobs as the value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_logs**
> GetExecutionLogsResponse get_task_logs(dataset_id, project_id, task_id, force_live=force_live)

Get task logs

Gets the log output from an individual task

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **project_id** | **str**|  | 
 **task_id** | **str**|  | 
 **force_live** | **bool**| force retrieving this info from the executor | [optional] [default to False]

### Return type

[**GetExecutionLogsResponse**](GetExecutionLogsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getTaskLogs 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_for_execution**
> List[Task] get_tasks_for_execution(dataset_id, project_id, force_live=force_live)

Get execution tasks

Gets the tasks submitted by the workflow execution

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **project_id** | **str**|  | 
 **force_live** | **bool**| force retrieving this info from the executor | [optional] [default to False]

### Return type

[**List[Task]**](Task.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getTasksForExecution 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_analysis**
> CreateResponse run_analysis(project_id, run_analysis_request)

Run analysis

Run analysis

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **run_analysis_request** | [**RunAnalysisRequest**](RunAnalysisRequest.md)|  | 

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
**200** | runAnalysis 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_analysis**
> StopExecutionResponse stop_analysis(dataset_id, project_id)

Stop execution

Terminates all analysis jobs related to this execution

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **project_id** | **str**|  | 

### Return type

[**StopExecutionResponse**](StopExecutionResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | stopAnalysis 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

