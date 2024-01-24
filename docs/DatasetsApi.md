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

