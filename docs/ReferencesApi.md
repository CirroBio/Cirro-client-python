# cirro_api_client.ReferencesApi

All URIs are relative to *https://api.cirro.bio*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_reference**](ReferencesApi.md#create_project_reference) | **POST** /projects/{projectId}/references | Create project reference
[**delete_project_reference**](ReferencesApi.md#delete_project_reference) | **DELETE** /projects/{projectId}/references | Delete project reference
[**get_reference_types**](ReferencesApi.md#get_reference_types) | **GET** /reference-types | Get reference types
[**get_references**](ReferencesApi.md#get_references) | **GET** /references | Get global references
[**get_references_for_project**](ReferencesApi.md#get_references_for_project) | **GET** /projects/{projectId}/references | Get project references
[**refresh_project_references**](ReferencesApi.md#refresh_project_references) | **PUT** /projects/{projectId}/references | Refresh project references


# **create_project_reference**
> Reference create_project_reference(project_id, create_reference_request)

Create project reference

Creates a reference

### Example

* Bearer (JWT) Authentication (accessToken):

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.create_reference_request import CreateReferenceRequest
from cirro_api_client.models.reference import Reference
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
    api_instance = cirro_api_client.ReferencesApi(api_client)
    project_id = 'project_id_example' # str | 
    create_reference_request = cirro_api_client.CreateReferenceRequest() # CreateReferenceRequest | 

    try:
        # Create project reference
        api_response = api_instance.create_project_reference(project_id, create_reference_request)
        print("The response of ReferencesApi->create_project_reference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->create_project_reference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_reference_request** | [**CreateReferenceRequest**](CreateReferenceRequest.md)|  | 

### Return type

[**Reference**](Reference.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createProjectReference 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_reference**
> delete_project_reference(project_id)

Delete project reference

Deletes a reference

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
    api_instance = cirro_api_client.ReferencesApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Delete project reference
        api_instance.delete_project_reference(project_id)
    except Exception as e:
        print("Exception when calling ReferencesApi->delete_project_reference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | deleteProjectReference 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_types**
> List[ReferenceType] get_reference_types()

Get reference types

List available reference types

### Example

* Bearer (JWT) Authentication (accessToken):

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.reference_type import ReferenceType
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
    api_instance = cirro_api_client.ReferencesApi(api_client)

    try:
        # Get reference types
        api_response = api_instance.get_reference_types()
        print("The response of ReferencesApi->get_reference_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->get_reference_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ReferenceType]**](ReferenceType.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getReferenceTypes 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_references**
> List[Reference] get_references()

Get global references

List available references (available to everyone)

### Example

* Bearer (JWT) Authentication (accessToken):

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.reference import Reference
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
    api_instance = cirro_api_client.ReferencesApi(api_client)

    try:
        # Get global references
        api_response = api_instance.get_references()
        print("The response of ReferencesApi->get_references:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->get_references: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Reference]**](Reference.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getReferences 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_references_for_project**
> List[Reference] get_references_for_project(project_id)

Get project references

List available references for a given project

### Example

* Bearer (JWT) Authentication (accessToken):

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.reference import Reference
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
    api_instance = cirro_api_client.ReferencesApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Get project references
        api_response = api_instance.get_references_for_project(project_id)
        print("The response of ReferencesApi->get_references_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferencesApi->get_references_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**List[Reference]**](Reference.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getReferencesForProject 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_project_references**
> refresh_project_references(project_id)

Refresh project references

Refresh project references (internal)

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
    api_instance = cirro_api_client.ReferencesApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Refresh project references
        api_instance.refresh_project_references(project_id)
    except Exception as e:
        print("Exception when calling ReferencesApi->refresh_project_references: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | refreshProjectReferences 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

