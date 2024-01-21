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

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.service_connection import ServiceConnection
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
    api_instance = cirro_api_client.SystemApi(api_client)

    try:
        # Get service connections
        api_response = api_instance.get_service_connections()
        print("The response of SystemApi->get_service_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_service_connections: %s\n" % e)
```



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

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.system_info_response import SystemInfoResponse
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
    api_instance = cirro_api_client.SystemApi(api_client)

    try:
        # Get system info
        api_response = api_instance.info()
        print("The response of SystemApi->info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->info: %s\n" % e)
```



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

