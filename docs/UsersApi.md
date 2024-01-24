# cirro_api_client.UsersApi

All URIs are relative to *https://api.cirro.bio*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user**](UsersApi.md#get_user) | **GET** /users/{username} | Get user
[**get_users**](UsersApi.md#get_users) | **GET** /users | List users
[**invite_user**](UsersApi.md#invite_user) | **POST** /users | Invite user
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{username} | Update user


# **get_user**
> User get_user(username)

Get user

Get user information

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getUser 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> List[User] get_users(username)

List users

Gets a list of users matching the username pattern

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username to filter on | 

### Return type

[**List[User]**](User.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getUsers 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_user**
> InviteUserResponse invite_user(invite_user_request)

Invite user

Invites a user to the system

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_user_request** | [**InviteUserRequest**](InviteUserRequest.md)|  | 

### Return type

[**InviteUserResponse**](InviteUserResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | inviteUser 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(username, update_user_request)

Update user

Update user information

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateUser 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

