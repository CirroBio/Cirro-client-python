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

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.create_notebook_instance_request import CreateNotebookInstanceRequest
from cirro_api_client.models.create_response import CreateResponse
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
    api_instance = cirro_api_client.NotebooksApi(api_client)
    project_id = 'project_id_example' # str | 
    create_notebook_instance_request = cirro_api_client.CreateNotebookInstanceRequest() # CreateNotebookInstanceRequest | 

    try:
        # Create notebook instance
        api_response = api_instance.create_notebook_instance(project_id, create_notebook_instance_request)
        print("The response of NotebooksApi->create_notebook_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotebooksApi->create_notebook_instance: %s\n" % e)
```



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

```python
import time
import os
import cirro_api_client
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
    api_instance = cirro_api_client.NotebooksApi(api_client)
    notebook_instance_id = 'notebook_instance_id_example' # str | 
    project_id = 'project_id_example' # str | 

    try:
        # Delete notebook instance
        api_instance.delete_notebook_instance(notebook_instance_id, project_id)
    except Exception as e:
        print("Exception when calling NotebooksApi->delete_notebook_instance: %s\n" % e)
```



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

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.open_notebook_instance_response import OpenNotebookInstanceResponse
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
    api_instance = cirro_api_client.NotebooksApi(api_client)
    notebook_instance_id = 'notebook_instance_id_example' # str | 
    project_id = 'project_id_example' # str | 

    try:
        # Generate notebook instance URL
        api_response = api_instance.generate_notebook_instance_url(notebook_instance_id, project_id)
        print("The response of NotebooksApi->generate_notebook_instance_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotebooksApi->generate_notebook_instance_url: %s\n" % e)
```



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

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.notebook_instance_status_response import NotebookInstanceStatusResponse
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
    api_instance = cirro_api_client.NotebooksApi(api_client)
    notebook_instance_id = 'notebook_instance_id_example' # str | 
    project_id = 'project_id_example' # str | 

    try:
        # Get notebook instance status
        api_response = api_instance.get_notebook_instance_status(notebook_instance_id, project_id)
        print("The response of NotebooksApi->get_notebook_instance_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotebooksApi->get_notebook_instance_status: %s\n" % e)
```



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

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.notebook_instance import NotebookInstance
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
    api_instance = cirro_api_client.NotebooksApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Get notebook instances
        api_response = api_instance.get_notebook_instances(project_id)
        print("The response of NotebooksApi->get_notebook_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotebooksApi->get_notebook_instances: %s\n" % e)
```



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

```python
import time
import os
import cirro_api_client
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
    api_instance = cirro_api_client.NotebooksApi(api_client)
    notebook_instance_id = 'notebook_instance_id_example' # str | 
    project_id = 'project_id_example' # str | 

    try:
        # Stop notebook instance
        api_instance.stop_notebook_instance(notebook_instance_id, project_id)
    except Exception as e:
        print("Exception when calling NotebooksApi->stop_notebook_instance: %s\n" % e)
```



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

