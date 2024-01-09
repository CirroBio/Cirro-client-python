# cirro_api_client.DatasetsApi

All URIs are relative to *https://api.cirro.bio*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dataset**](DatasetsApi.md#delete_dataset) | **DELETE** /projects/{projectId}/datasets/{datasetId} | Delete a dataset
[**get_dataset**](DatasetsApi.md#get_dataset) | **GET** /projects/{projectId}/datasets/{datasetId} | Get dataset
[**get_dataset_manifest**](DatasetsApi.md#get_dataset_manifest) | **GET** /projects/{projectId}/datasets/{datasetId}/files | Get dataset manifest
[**get_datasets**](DatasetsApi.md#get_datasets) | **GET** /projects/{projectId}/datasets | List datasets
[**import_public_dataset**](DatasetsApi.md#import_public_dataset) | **POST** /projects/{projectId}/datasets/import | Import public dataset
[**ingest_samples**](DatasetsApi.md#ingest_samples) | **PUT** /projects/{projectId}/datasets/{datasetId}/ingest-samples | Rerun sample ingest
[**regenerate_manifest**](DatasetsApi.md#regenerate_manifest) | **PUT** /projects/{projectId}/datasets/{datasetId}/regenerate-manifest | Regenerate dataset manifest
[**rerun_transform**](DatasetsApi.md#rerun_transform) | **PUT** /projects/{projectId}/datasets/{datasetId}/rerun-transform | Rerun data transforms
[**update_dataset**](DatasetsApi.md#update_dataset) | **PUT** /projects/{projectId}/datasets/{datasetId} | Update dataset
[**upload_dataset**](DatasetsApi.md#upload_dataset) | **POST** /projects/{projectId}/datasets/upload | Upload private dataset


# **delete_dataset**
> delete_dataset(project_id, dataset_id)

Delete a dataset

Deletes the dataset, files are saved according to the project's retention time.

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
    api_instance = cirro_api_client.DatasetsApi(api_client)
    project_id = 'project_id_example' # str | 
    dataset_id = 'dataset_id_example' # str | 

    try:
        # Delete a dataset
        api_instance.delete_dataset(project_id, dataset_id)
    except Exception as e:
        print("Exception when calling DatasetsApi->delete_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **dataset_id** | **str**|  | 

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
**200** | deleteDataset 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset**
> DatasetDetail get_dataset(dataset_id, project_id)

Get dataset

Gets detailed information about a dataset

### Example

* Bearer (JWT) Authentication (accessToken):

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.dataset_detail import DatasetDetail
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
    api_instance = cirro_api_client.DatasetsApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
    project_id = 'project_id_example' # str | 

    try:
        # Get dataset
        api_response = api_instance.get_dataset(dataset_id, project_id)
        print("The response of DatasetsApi->get_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **project_id** | **str**|  | 

### Return type

[**DatasetDetail**](DatasetDetail.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getDataset 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_manifest**
> DatasetAssetsManifest get_dataset_manifest(dataset_id, project_id)

Get dataset manifest

Gets a listing of files, charts, and other assets available for the dataset

### Example

* Bearer (JWT) Authentication (accessToken):

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.dataset_assets_manifest import DatasetAssetsManifest
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
    api_instance = cirro_api_client.DatasetsApi(api_client)
    dataset_id = 'dataset_id_example' # str | 
    project_id = 'project_id_example' # str | 

    try:
        # Get dataset manifest
        api_response = api_instance.get_dataset_manifest(dataset_id, project_id)
        print("The response of DatasetsApi->get_dataset_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_dataset_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **project_id** | **str**|  | 

### Return type

[**DatasetAssetsManifest**](DatasetAssetsManifest.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getDatasetManifest 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasets**
> PaginatedResponseDatasetListDto get_datasets(project_id, limit=limit, next_token=next_token)

List datasets

Retrieves a list of datasets for a given project

### Example

* Bearer (JWT) Authentication (accessToken):

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.paginated_response_dataset_list_dto import PaginatedResponseDatasetListDto
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
    api_instance = cirro_api_client.DatasetsApi(api_client)
    project_id = 'project_id_example' # str | 
    limit = 10000 # int | number of records to get (optional) (default to 10000)
    next_token = 'next_token_example' # str | cursor to request the next page (optional)

    try:
        # List datasets
        api_response = api_instance.get_datasets(project_id, limit=limit, next_token=next_token)
        print("The response of DatasetsApi->get_datasets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_datasets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **limit** | **int**| number of records to get | [optional] [default to 10000]
 **next_token** | **str**| cursor to request the next page | [optional] 

### Return type

[**PaginatedResponseDatasetListDto**](PaginatedResponseDatasetListDto.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getDatasets 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_public_dataset**
> CreateResponse import_public_dataset(project_id, import_data_request)

Import public dataset

Download data from public repositories

### Example

* Bearer (JWT) Authentication (accessToken):

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.create_response import CreateResponse
from cirro_api_client.models.import_data_request import ImportDataRequest
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
    api_instance = cirro_api_client.DatasetsApi(api_client)
    project_id = 'project_id_example' # str | 
    import_data_request = cirro_api_client.ImportDataRequest() # ImportDataRequest | 

    try:
        # Import public dataset
        api_response = api_instance.import_public_dataset(project_id, import_data_request)
        print("The response of DatasetsApi->import_public_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->import_public_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **import_data_request** | [**ImportDataRequest**](ImportDataRequest.md)|  | 

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
**200** | importPublicDataset 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ingest_samples**
> ingest_samples(project_id, dataset_id)

Rerun sample ingest

Rerun sample ingest (TODO).

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
    api_instance = cirro_api_client.DatasetsApi(api_client)
    project_id = 'project_id_example' # str | 
    dataset_id = 'dataset_id_example' # str | 

    try:
        # Rerun sample ingest
        api_instance.ingest_samples(project_id, dataset_id)
    except Exception as e:
        print("Exception when calling DatasetsApi->ingest_samples: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **dataset_id** | **str**|  | 

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
**200** | ingestSamples 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_manifest**
> regenerate_manifest(project_id, dataset_id)

Regenerate dataset manifest

Regenerate dataset manifest (TODO).

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
    api_instance = cirro_api_client.DatasetsApi(api_client)
    project_id = 'project_id_example' # str | 
    dataset_id = 'dataset_id_example' # str | 

    try:
        # Regenerate dataset manifest
        api_instance.regenerate_manifest(project_id, dataset_id)
    except Exception as e:
        print("Exception when calling DatasetsApi->regenerate_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **dataset_id** | **str**|  | 

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
**200** | regenerateManifest 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rerun_transform**
> rerun_transform(project_id, dataset_id)

Rerun data transforms

Rerun data transforms (TODO).

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
    api_instance = cirro_api_client.DatasetsApi(api_client)
    project_id = 'project_id_example' # str | 
    dataset_id = 'dataset_id_example' # str | 

    try:
        # Rerun data transforms
        api_instance.rerun_transform(project_id, dataset_id)
    except Exception as e:
        print("Exception when calling DatasetsApi->rerun_transform: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **dataset_id** | **str**|  | 

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
**200** | rerunTransform 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset**
> DatasetDetail update_dataset(project_id, dataset_id, update_dataset_request)

Update dataset

Update info on a dataset

### Example

* Bearer (JWT) Authentication (accessToken):

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.dataset_detail import DatasetDetail
from cirro_api_client.models.update_dataset_request import UpdateDatasetRequest
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
    api_instance = cirro_api_client.DatasetsApi(api_client)
    project_id = 'project_id_example' # str | 
    dataset_id = 'dataset_id_example' # str | 
    update_dataset_request = cirro_api_client.UpdateDatasetRequest() # UpdateDatasetRequest | 

    try:
        # Update dataset
        api_response = api_instance.update_dataset(project_id, dataset_id, update_dataset_request)
        print("The response of DatasetsApi->update_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->update_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **dataset_id** | **str**|  | 
 **update_dataset_request** | [**UpdateDatasetRequest**](UpdateDatasetRequest.md)|  | 

### Return type

[**DatasetDetail**](DatasetDetail.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateDataset 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_dataset**
> UploadDatasetCreateResponse upload_dataset(project_id, upload_dataset_request)

Upload private dataset

Registers a dataset in the system that you upload files into

### Example

* Bearer (JWT) Authentication (accessToken):

```python
import time
import os
import cirro_api_client
from cirro_api_client.models.upload_dataset_create_response import UploadDatasetCreateResponse
from cirro_api_client.models.upload_dataset_request import UploadDatasetRequest
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
    api_instance = cirro_api_client.DatasetsApi(api_client)
    project_id = 'project_id_example' # str | 
    upload_dataset_request = cirro_api_client.UploadDatasetRequest() # UploadDatasetRequest | 

    try:
        # Upload private dataset
        api_response = api_instance.upload_dataset(project_id, upload_dataset_request)
        print("The response of DatasetsApi->upload_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->upload_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **upload_dataset_request** | [**UploadDatasetRequest**](UploadDatasetRequest.md)|  | 

### Return type

[**UploadDatasetCreateResponse**](UploadDatasetCreateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | uploadDataset 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

