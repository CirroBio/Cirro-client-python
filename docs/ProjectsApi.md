# cirro_api_client.ProjectsApi

All URIs are relative to *https://api.cirro.bio*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectsApi.md#create_project) | **POST** /projects | Create project
[**get_project**](ProjectsApi.md#get_project) | **GET** /projects/{projectId} | Get project
[**get_project_users**](ProjectsApi.md#get_project_users) | **GET** /projects/{projectId}/permissions | Get project permissions
[**get_projects**](ProjectsApi.md#get_projects) | **GET** /projects | Get projects
[**redeploy_project**](ProjectsApi.md#redeploy_project) | **PUT** /projects/{projectId}:re-deploy | Redeploy project
[**set_user_project_role**](ProjectsApi.md#set_user_project_role) | **PUT** /projects/{projectId}/permissions | Set role
[**update_project**](ProjectsApi.md#update_project) | **PUT** /projects/{projectId} | Update project
[**update_project_tags**](ProjectsApi.md#update_project_tags) | **PUT** /projects/{projectId}:tags | Set project tags


# **create_project**
> CreateResponse create_project(project_request)

Create project

Creates a project

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_request** | [**ProjectRequest**](ProjectRequest.md)|  | 

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
**200** | createProject 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> ProjectDetail get_project(project_id)

Get project

Get detailed project information

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**ProjectDetail**](ProjectDetail.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getProject 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_users**
> List[ProjectUser] get_project_users(project_id)

Get project permissions

Gets users who have access to the project

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**List[ProjectUser]**](ProjectUser.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getProjectUsers 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> List[Project] get_projects()

Get projects

Retrieve a list of projects

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Project]**](Project.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | getProjects 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeploy_project**
> redeploy_project(project_id)

Redeploy project

Redeploys cloud resources for a project

### Example

* Bearer (JWT) Authentication (accessToken):

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
**200** | redeployProject 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_project_role**
> set_user_project_role(project_id, set_user_project_role_request)

Set role

Sets a user's role within a project

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **set_user_project_role_request** | [**SetUserProjectRoleRequest**](SetUserProjectRoleRequest.md)|  | 

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
**200** | setUserProjectRole 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> ProjectDetail update_project(project_id, project_request)

Update project

Updates a project

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **project_request** | [**ProjectRequest**](ProjectRequest.md)|  | 

### Return type

[**ProjectDetail**](ProjectDetail.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateProject 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_tags**
> update_project_tags(project_id, tag)

Set project tags

Sets tags on a project

### Example

* Bearer (JWT) Authentication (accessToken):

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tag** | [**List[Tag]**](Tag.md)|  | 

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
**200** | updateProjectTags 200 response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

