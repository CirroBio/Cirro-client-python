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

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.get_execution_logs_response import GetExecutionLogsResponse
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
    api_instance = cirro_api_client.ExecutionApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
    project_id = 'project_id_example' # str | 
    force_live = False # bool | force retrieving this info from the executor (optional) (default to False)

    try:
        # Get execution logs
        api_response = api_instance.get_execution_logs(dataset_id, project_id, force_live=force_live)
        print("The response of ExecutionApi->get_execution_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionApi->get_execution_logs: %s\n" % e)
```



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

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.task import Task
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
    api_instance = cirro_api_client.ExecutionApi(api_client)
    project_id = 'project_id_example' # str | 
    number_of_days = 1 # int | Number of days of job history to pull (optional) (default to 1)

    try:
        # Get execution summary
        api_response = api_instance.get_project_summary(project_id, number_of_days=number_of_days)
        print("The response of ExecutionApi->get_project_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionApi->get_project_summary: %s\n" % e)
```



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

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.get_execution_logs_response import GetExecutionLogsResponse
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
    api_instance = cirro_api_client.ExecutionApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
    project_id = 'project_id_example' # str | 
    task_id = 'task_id_example' # str | 
    force_live = False # bool | force retrieving this info from the executor (optional) (default to False)

    try:
        # Get task logs
        api_response = api_instance.get_task_logs(dataset_id, project_id, task_id, force_live=force_live)
        print("The response of ExecutionApi->get_task_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionApi->get_task_logs: %s\n" % e)
```



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

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.task import Task
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
    api_instance = cirro_api_client.ExecutionApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
    project_id = 'project_id_example' # str | 
    force_live = False # bool | force retrieving this info from the executor (optional) (default to False)

    try:
        # Get execution tasks
        api_response = api_instance.get_tasks_for_execution(dataset_id, project_id, force_live=force_live)
        print("The response of ExecutionApi->get_tasks_for_execution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionApi->get_tasks_for_execution: %s\n" % e)
```



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

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.create_response import CreateResponse
from cirro_api_client.models.run_analysis_request import RunAnalysisRequest
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
    api_instance = cirro_api_client.ExecutionApi(api_client)
    project_id = 'project_id_example' # str | 
    run_analysis_request = cirro_api_client.RunAnalysisRequest() # RunAnalysisRequest | 

    try:
        # Run analysis
        api_response = api_instance.run_analysis(project_id, run_analysis_request)
        print("The response of ExecutionApi->run_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionApi->run_analysis: %s\n" % e)
```



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

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.stop_execution_response import StopExecutionResponse
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
    api_instance = cirro_api_client.ExecutionApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
    project_id = 'project_id_example' # str | 

    try:
        # Stop execution
        api_response = api_instance.stop_analysis(dataset_id, project_id)
        print("The response of ExecutionApi->stop_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionApi->stop_analysis: %s\n" % e)
```



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

