# cirro-api-client
Cirro Data Platform service API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: latest
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://cirro.bio](https://cirro.bio)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cirro_api_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cirro_api_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
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
    api_instance = cirro_api_client.BillingApi(api_client)
    billing_account_request = cirro_api_client.BillingAccountRequest() # BillingAccountRequest | 

    try:
        # Create billing account
        api_response = api_instance.create_billing_account(billing_account_request)
        print("The response of BillingApi->create_billing_account:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->create_billing_account: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.cirro.bio*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BillingApi* | [**create_billing_account**](docs/BillingApi.md#create_billing_account) | **POST** /billing | Create billing account
*BillingApi* | [**delete_billing_account**](docs/BillingApi.md#delete_billing_account) | **DELETE** /billing/{billingAccountId} | Delete billing account
*BillingApi* | [**generate_billing_report**](docs/BillingApi.md#generate_billing_report) | **GET** /billing-report | Generate billing report
*BillingApi* | [**get_billing_accounts**](docs/BillingApi.md#get_billing_accounts) | **GET** /billing | List billing accounts
*BillingApi* | [**update_billing_account**](docs/BillingApi.md#update_billing_account) | **PUT** /billing/{billingAccountId} | Update billing account
*DashboardsApi* | [**create_dashboard**](docs/DashboardsApi.md#create_dashboard) | **POST** /projects/{projectId}/dashboards | Create dashboard
*DashboardsApi* | [**delete_dashboard**](docs/DashboardsApi.md#delete_dashboard) | **DELETE** /projects/{projectId}/dashboards/{dashboardId} | Delete dashboard
*DashboardsApi* | [**get_dashboard**](docs/DashboardsApi.md#get_dashboard) | **GET** /projects/{projectId}/dashboards/{dashboardId} | Get dashboard
*DashboardsApi* | [**get_dashboards**](docs/DashboardsApi.md#get_dashboards) | **GET** /projects/{projectId}/dashboards | List dashboards
*DashboardsApi* | [**update_dashboard**](docs/DashboardsApi.md#update_dashboard) | **PUT** /projects/{projectId}/dashboards/{dashboardId} | Update dashboard
*DatasetsApi* | [**delete_dataset**](docs/DatasetsApi.md#delete_dataset) | **DELETE** /projects/{projectId}/datasets/{datasetId} | Delete a dataset
*DatasetsApi* | [**get_dataset**](docs/DatasetsApi.md#get_dataset) | **GET** /projects/{projectId}/datasets/{datasetId} | Get dataset
*DatasetsApi* | [**get_dataset_manifest**](docs/DatasetsApi.md#get_dataset_manifest) | **GET** /projects/{projectId}/datasets/{datasetId}/files | Get dataset manifest
*DatasetsApi* | [**get_datasets**](docs/DatasetsApi.md#get_datasets) | **GET** /projects/{projectId}/datasets | List datasets
*DatasetsApi* | [**import_public_dataset**](docs/DatasetsApi.md#import_public_dataset) | **POST** /projects/{projectId}/datasets/import | Import public dataset
*DatasetsApi* | [**ingest_samples**](docs/DatasetsApi.md#ingest_samples) | **PUT** /projects/{projectId}/datasets/{datasetId}/ingest-samples | Rerun sample ingest
*DatasetsApi* | [**regenerate_manifest**](docs/DatasetsApi.md#regenerate_manifest) | **PUT** /projects/{projectId}/datasets/{datasetId}/regenerate-manifest | Regenerate dataset manifest
*DatasetsApi* | [**rerun_transform**](docs/DatasetsApi.md#rerun_transform) | **PUT** /projects/{projectId}/datasets/{datasetId}/rerun-transform | Rerun data transforms
*DatasetsApi* | [**update_dataset**](docs/DatasetsApi.md#update_dataset) | **PUT** /projects/{projectId}/datasets/{datasetId} | Update dataset
*DatasetsApi* | [**upload_dataset**](docs/DatasetsApi.md#upload_dataset) | **POST** /projects/{projectId}/datasets/upload | Upload private dataset
*ExecutionApi* | [**get_execution_logs**](docs/ExecutionApi.md#get_execution_logs) | **GET** /projects/{projectId}/execution/{datasetId}/logs | Get execution logs
*ExecutionApi* | [**get_project_summary**](docs/ExecutionApi.md#get_project_summary) | **GET** /projects/{projectId}/execution | Get execution summary
*ExecutionApi* | [**get_task_logs**](docs/ExecutionApi.md#get_task_logs) | **GET** /projects/{projectId}/execution/{datasetId}/tasks/{taskId}/logs | Get task logs
*ExecutionApi* | [**get_tasks_for_execution**](docs/ExecutionApi.md#get_tasks_for_execution) | **GET** /projects/{projectId}/execution/{datasetId}/tasks | Get execution tasks
*ExecutionApi* | [**run_analysis**](docs/ExecutionApi.md#run_analysis) | **POST** /projects/{projectId}/execution | Run analysis
*ExecutionApi* | [**stop_analysis**](docs/ExecutionApi.md#stop_analysis) | **PUT** /projects/{projectId}/execution/{datasetId}/stop | Stop execution
*FileApi* | [**generate_sftp_token**](docs/FileApi.md#generate_sftp_token) | **POST** /projects/{projectId}/sftp-token | Create SFTP Token
*MetadataApi* | [**get_project_samples**](docs/MetadataApi.md#get_project_samples) | **GET** /projects/{projectId}/samples | Get project samples
*MetadataApi* | [**get_project_schema**](docs/MetadataApi.md#get_project_schema) | **GET** /projects/{projectId}/schema | Get project metadata schema
*MetadataApi* | [**update_project_schema**](docs/MetadataApi.md#update_project_schema) | **PUT** /projects/{projectId}/schema | Update project metadata schema
*MetadataApi* | [**update_sample**](docs/MetadataApi.md#update_sample) | **PUT** /projects/{projectId}/samples/{sampleId} | Update sample
*MetricsApi* | [**get_all_metrics**](docs/MetricsApi.md#get_all_metrics) | **GET** /metrics | Get all project metrics
*MetricsApi* | [**get_project_metrics**](docs/MetricsApi.md#get_project_metrics) | **GET** /projects/{projectId}/metrics | Get project metrics
*NotebooksApi* | [**create_notebook_instance**](docs/NotebooksApi.md#create_notebook_instance) | **POST** /projects/{projectId}/notebook-instances | Create notebook instance
*NotebooksApi* | [**delete_notebook_instance**](docs/NotebooksApi.md#delete_notebook_instance) | **DELETE** /projects/{projectId}/notebook-instances/{notebookInstanceId} | Delete notebook instance
*NotebooksApi* | [**generate_notebook_instance_url**](docs/NotebooksApi.md#generate_notebook_instance_url) | **GET** /projects/{projectId}/notebook-instances/{notebookInstanceId}:generate-url | Generate notebook instance URL
*NotebooksApi* | [**get_notebook_instance_status**](docs/NotebooksApi.md#get_notebook_instance_status) | **GET** /projects/{projectId}/notebook-instances/{notebookInstanceId}:status | Get notebook instance status
*NotebooksApi* | [**get_notebook_instances**](docs/NotebooksApi.md#get_notebook_instances) | **GET** /projects/{projectId}/notebook-instances | Get notebook instances
*NotebooksApi* | [**stop_notebook_instance**](docs/NotebooksApi.md#stop_notebook_instance) | **POST** /projects/{projectId}/notebook-instances/{notebookInstanceId}:stop | Stop notebook instance
*ProcessesApi* | [**get_process**](docs/ProcessesApi.md#get_process) | **GET** /processes/{processId} | Get process
*ProcessesApi* | [**get_process_parameters**](docs/ProcessesApi.md#get_process_parameters) | **GET** /processes/{processId}/parameters | Get process parameters
*ProcessesApi* | [**get_processes**](docs/ProcessesApi.md#get_processes) | **GET** /processes | List processes
*ProcessesApi* | [**validate_file_requirements**](docs/ProcessesApi.md#validate_file_requirements) | **POST** /processes/{processId}/validate-files | Validate file requirements
*ProjectsApi* | [**create_project**](docs/ProjectsApi.md#create_project) | **POST** /projects | Create project
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /projects/{projectId} | Get project
*ProjectsApi* | [**get_project_users**](docs/ProjectsApi.md#get_project_users) | **GET** /projects/{projectId}/permissions | Get project permissions
*ProjectsApi* | [**get_projects**](docs/ProjectsApi.md#get_projects) | **GET** /projects | Get projects
*ProjectsApi* | [**redeploy_project**](docs/ProjectsApi.md#redeploy_project) | **PUT** /projects/{projectId}:re-deploy | Redeploy project
*ProjectsApi* | [**set_user_project_role**](docs/ProjectsApi.md#set_user_project_role) | **PUT** /projects/{projectId}/permissions | Set role
*ProjectsApi* | [**update_project**](docs/ProjectsApi.md#update_project) | **PUT** /projects/{projectId} | Update project
*ProjectsApi* | [**update_project_tags**](docs/ProjectsApi.md#update_project_tags) | **PUT** /projects/{projectId}:tags | Set project tags
*ReferencesApi* | [**get_reference_types**](docs/ReferencesApi.md#get_reference_types) | **GET** /reference-types | Get reference types
*ReferencesApi* | [**get_references**](docs/ReferencesApi.md#get_references) | **GET** /references | Get global references
*ReferencesApi* | [**get_references_for_project**](docs/ReferencesApi.md#get_references_for_project) | **GET** /projects/{projectId}/references | Get project references
*SystemApi* | [**get_service_connections**](docs/SystemApi.md#get_service_connections) | **GET** /service-connections | Get service connections
*SystemApi* | [**info**](docs/SystemApi.md#info) | **GET** /info | Get system info
*SystemApi* | [**info1**](docs/SystemApi.md#info1) | **GET** /info/system | Get system info
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /users/{username} | Get user
*UsersApi* | [**get_users**](docs/UsersApi.md#get_users) | **GET** /users | List users
*UsersApi* | [**invite_user**](docs/UsersApi.md#invite_user) | **POST** /users | Invite user
*UsersApi* | [**update_user**](docs/UsersApi.md#update_user) | **PUT** /users/{username} | Update user


## Documentation For Models

 - [AllowedDataType](docs/AllowedDataType.md)
 - [BillingAccount](docs/BillingAccount.md)
 - [BillingAccountRequest](docs/BillingAccountRequest.md)
 - [BillingMethod](docs/BillingMethod.md)
 - [BudgetPeriod](docs/BudgetPeriod.md)
 - [CloudAccount](docs/CloudAccount.md)
 - [Contact](docs/Contact.md)
 - [CreateNotebookInstanceRequest](docs/CreateNotebookInstanceRequest.md)
 - [CreateResponse](docs/CreateResponse.md)
 - [CustomPipelineSettings](docs/CustomPipelineSettings.md)
 - [CustomerType](docs/CustomerType.md)
 - [Dashboard](docs/Dashboard.md)
 - [DashboardRequest](docs/DashboardRequest.md)
 - [Dataset](docs/Dataset.md)
 - [DatasetAssetsManifest](docs/DatasetAssetsManifest.md)
 - [DatasetDetail](docs/DatasetDetail.md)
 - [DatasetFile](docs/DatasetFile.md)
 - [DatasetViz](docs/DatasetViz.md)
 - [Executor](docs/Executor.md)
 - [FileNamePattern](docs/FileNamePattern.md)
 - [FileRequirements](docs/FileRequirements.md)
 - [FormSchema](docs/FormSchema.md)
 - [GenerateSftpCredentialsRequest](docs/GenerateSftpCredentialsRequest.md)
 - [GetExecutionLogsResponse](docs/GetExecutionLogsResponse.md)
 - [ImportDataRequest](docs/ImportDataRequest.md)
 - [InviteUserRequest](docs/InviteUserRequest.md)
 - [InviteUserResponse](docs/InviteUserResponse.md)
 - [LogEntry](docs/LogEntry.md)
 - [MetricRecord](docs/MetricRecord.md)
 - [NotebookInstance](docs/NotebookInstance.md)
 - [NotebookInstanceStatusResponse](docs/NotebookInstanceStatusResponse.md)
 - [OpenNotebookInstanceResponse](docs/OpenNotebookInstanceResponse.md)
 - [PaginatedResponseDatasetListDto](docs/PaginatedResponseDatasetListDto.md)
 - [PaginatedResponseSampleDto](docs/PaginatedResponseSampleDto.md)
 - [Process](docs/Process.md)
 - [ProcessDetail](docs/ProcessDetail.md)
 - [Project](docs/Project.md)
 - [ProjectDetail](docs/ProjectDetail.md)
 - [ProjectMetrics](docs/ProjectMetrics.md)
 - [ProjectRequest](docs/ProjectRequest.md)
 - [ProjectRole](docs/ProjectRole.md)
 - [ProjectSettings](docs/ProjectSettings.md)
 - [ProjectUser](docs/ProjectUser.md)
 - [Reference](docs/Reference.md)
 - [ReferenceType](docs/ReferenceType.md)
 - [RunAnalysisRequest](docs/RunAnalysisRequest.md)
 - [Sample](docs/Sample.md)
 - [SampleRequest](docs/SampleRequest.md)
 - [ServiceConnection](docs/ServiceConnection.md)
 - [SetUserProjectRoleRequest](docs/SetUserProjectRoleRequest.md)
 - [SftpCredentials](docs/SftpCredentials.md)
 - [Status](docs/Status.md)
 - [StopExecutionResponse](docs/StopExecutionResponse.md)
 - [SystemInfoResponse](docs/SystemInfoResponse.md)
 - [Tag](docs/Tag.md)
 - [Task](docs/Task.md)
 - [UpdateDatasetRequest](docs/UpdateDatasetRequest.md)
 - [UpdateUserRequest](docs/UpdateUserRequest.md)
 - [UploadDatasetCreateResponse](docs/UploadDatasetCreateResponse.md)
 - [UploadDatasetRequest](docs/UploadDatasetRequest.md)
 - [User](docs/User.md)
 - [ValidateFileRequirementsRequest](docs/ValidateFileRequirementsRequest.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="accessToken"></a>
### accessToken

- **Type**: Bearer authentication (JWT)


## Author

support@cirro.bio


