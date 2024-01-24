# cirro_api_client.BillingApi

All URIs are relative to *https://api.cirro.bio*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_billing_account**](BillingApi.md#create_billing_account) | **POST** /billing | Create billing account
[**delete_billing_account**](BillingApi.md#delete_billing_account) | **DELETE** /billing/{billingAccountId} | Delete billing account
[**generate_billing_report**](BillingApi.md#generate_billing_report) | **GET** /billing-report | Generate billing report
[**get_billing_accounts**](BillingApi.md#get_billing_accounts) | **GET** /billing | List billing accounts
[**update_billing_account**](BillingApi.md#update_billing_account) | **PUT** /billing/{billingAccountId} | Update billing account


# **create_billing_account**
> CreateResponse create_billing_account(billing_account_request)

Create billing account

Creates a billing account

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_account_request** | [**BillingAccountRequest**](BillingAccountRequest.md)|  | 

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
**200** | createBillingAccount 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_billing_account**
> delete_billing_account(billing_account_id)

Delete billing account

Deletes a billing account

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_account_id** | **str**|  | 

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
**200** | deleteBillingAccount 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_billing_report**
> generate_billing_report()

Generate billing report

Generates a billing report xlsx with cost information

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ms-excel

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_accounts**
> List[BillingAccount] get_billing_accounts(include_archived=include_archived)

List billing accounts

Gets a list of billing accounts the current user has access to

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_archived** | **bool**| Include billing accounts that are no longer in use | [optional] [default to False]

### Return type

[**List[BillingAccount]**](BillingAccount.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getBillingAccounts 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_account**
> update_billing_account(billing_account_id, billing_account_request)

Update billing account

Updates a billing account

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_account_id** | **str**|  | 
 **billing_account_request** | [**BillingAccountRequest**](BillingAccountRequest.md)|  | 

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
**200** | updateBillingAccount 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

