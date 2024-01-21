# ProjectSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_amount** | **int** | Total allowed cost for the budget period | [optional] 
**budget_period** | [**BudgetPeriod**](BudgetPeriod.md) |  | [optional] 
**dragen_ami** | **str** | AMI ID for the DRAGEN compute environment (if enabled) | [optional] 
**enable_compute** | **bool** | Enables the default compute environment | [optional] [default to True]
**enable_dragen** | **bool** | Enables the DRAGEN compute environment | [optional] [default to False]
**enable_backup** | **bool** | Enables the AWS Backup service for S3 | [optional] [default to False]
**enable_sftp** | **bool** | Enables access to files over SFTP | [optional] [default to False]
**max_f1_vcpu** | **int** | Service quota limit for On Demand F1 instances | [optional] [default to 0]
**max_spot_vcpu** | **int** | Service quota limit for SPOT instances | [optional] [default to 0]
**retention_policy_days** | **int** | Days to keep deleted datasets before being permanently erased | [optional] [default to 7]
**service_connections** | **List[str]** |  | 
**create_vpc** | **bool** | Creates a default VPC for the compute environment, if false, VPC ID must be provided | [optional] [default to False]
**vpc_id** | **str** | VPC that the compute environment will use | [optional] 
**batch_subnets** | **List[str]** | List of subnets that the compute environment will use | [optional] 
**kms_arn** | **str** | KMS Key ARN to encrypt S3 objects, one will be created if the arn is not provided | [optional] 

## Example

```python
from cirro_api_client.models.project_settings import ProjectSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSettings from a JSON string
project_settings_instance = ProjectSettings.from_json(json)
# print the JSON string representation of the object
print ProjectSettings.to_json()

# convert the object into a dict
project_settings_dict = project_settings_instance.to_dict()
# create an instance of ProjectSettings from a dict
project_settings_form_dict = project_settings.from_dict(project_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


