# cirro_api_client.ProcessesApi

All URIs are relative to *https://api.cirro.bio*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_process**](ProcessesApi.md#get_process) | **GET** /processes/{processId} | Get process
[**get_process_parameters**](ProcessesApi.md#get_process_parameters) | **GET** /processes/{processId}/parameters | Get process parameters
[**get_processes**](ProcessesApi.md#get_processes) | **GET** /processes | List processes
[**validate_file_requirements**](ProcessesApi.md#validate_file_requirements) | **POST** /processes/{processId}/validate-files | Validate file requirements


# **get_process**
> ProcessDetail get_process(process_id)

Get process

Retrieves detailed information on a process

### Example

* Bearer (JWT) Authentication (accessToken):

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.process_detail import ProcessDetail
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
    api_instance = cirro_api_client.ProcessesApi(api_client)
    process_id = 'process_id_example' # str | 

    try:
        # Get process
        api_response = api_instance.get_process(process_id)
        print("The response of ProcessesApi->get_process:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessesApi->get_process: %s\n" % e)
```



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

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.form_schema import FormSchema
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
    api_instance = cirro_api_client.ProcessesApi(api_client)
    process_id = 'process_id_example' # str | 

    try:
        # Get process parameters
        api_response = api_instance.get_process_parameters(process_id)
        print("The response of ProcessesApi->get_process_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessesApi->get_process_parameters: %s\n" % e)
```



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

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.process import Process
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
    api_instance = cirro_api_client.ProcessesApi(api_client)
    include_archived = False # bool | Include processes that are no longer in use (optional) (default to False)

    try:
        # List processes
        api_response = api_instance.get_processes(include_archived=include_archived)
        print("The response of ProcessesApi->get_processes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessesApi->get_processes: %s\n" % e)
```



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

# **validate_file_requirements**
> FileRequirements validate_file_requirements(process_id, validate_file_requirements_request)

Validate file requirements

Checks the input file names with the expected files for a data type (ingest processes only)

### Example

* Bearer (JWT) Authentication (accessToken):

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.file_requirements import FileRequirements
from cirro_api_client.models.validate_file_requirements_request import ValidateFileRequirementsRequest
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
    api_instance = cirro_api_client.ProcessesApi(api_client)
    process_id = 'process_id_example' # str | 
    validate_file_requirements_request = cirro_api_client.ValidateFileRequirementsRequest() # ValidateFileRequirementsRequest | 

    try:
        # Validate file requirements
        api_response = api_instance.validate_file_requirements(process_id, validate_file_requirements_request)
        print("The response of ProcessesApi->validate_file_requirements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessesApi->validate_file_requirements: %s\n" % e)
```



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

