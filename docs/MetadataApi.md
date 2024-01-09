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

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.paginated_response_sample_dto import PaginatedResponseSampleDto
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
    api_instance = cirro_api_client.MetadataApi(api_client)
    project_id = 'project_id_example' # str | 
    limit = 10000 # int | number of records to get (optional) (default to 10000)
    next_token = 'next_token_example' # str | cursor to request the next page (optional)

    try:
        # Get project samples
        api_response = api_instance.get_project_samples(project_id, limit=limit, next_token=next_token)
        print("The response of MetadataApi->get_project_samples:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_project_samples: %s\n" % e)
```



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
    api_instance = cirro_api_client.MetadataApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Get project metadata schema
        api_response = api_instance.get_project_schema(project_id)
        print("The response of MetadataApi->get_project_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_project_schema: %s\n" % e)
```



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
    api_instance = cirro_api_client.MetadataApi(api_client)
    project_id = 'project_id_example' # str | 
    form_schema = cirro_api_client.FormSchema() # FormSchema | 

    try:
        # Update project metadata schema
        api_instance.update_project_schema(project_id, form_schema)
    except Exception as e:
        print("Exception when calling MetadataApi->update_project_schema: %s\n" % e)
```



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

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.sample import Sample
from cirro_api_client.models.sample_request import SampleRequest
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
    api_instance = cirro_api_client.MetadataApi(api_client)
    project_id = 'project_id_example' # str | 
    sample_id = 'sample_id_example' # str | 
    sample_request = cirro_api_client.SampleRequest() # SampleRequest | 

    try:
        # Update sample
        api_response = api_instance.update_sample(project_id, sample_id, sample_request)
        print("The response of MetadataApi->update_sample:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->update_sample: %s\n" % e)
```



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

