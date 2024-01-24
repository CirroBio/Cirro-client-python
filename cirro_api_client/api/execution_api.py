# coding: utf-8

"""
    Cirro Data

    Cirro Data Platform service API

    The version of the OpenAPI document: latest
    Contact: support@cirro.bio
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictBool, StrictInt, StrictStr

from typing import Dict, List, Optional

from cirro_api_client.models.create_response import CreateResponse
from cirro_api_client.models.get_execution_logs_response import GetExecutionLogsResponse
from cirro_api_client.models.run_analysis_request import RunAnalysisRequest
from cirro_api_client.models.stop_execution_response import StopExecutionResponse
from cirro_api_client.models.task import Task

from cirro_api_client.api_client import ApiClient, RequestSerialized
from cirro_api_client.api_response import ApiResponse


class ExecutionApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def get_execution_logs(
        self,
        dataset_id: StrictStr,
        project_id: StrictStr,
        force_live: Annotated[Optional[StrictBool], Field(description="force retrieving this info from the executor")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> GetExecutionLogsResponse:
        """Get execution logs

        Gets live logs from main execution task

        :param dataset_id: (required)
        :type dataset_id: str
        :param project_id: (required)
        :type project_id: str
        :param force_live: force retrieving this info from the executor
        :type force_live: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :return: Returns the result object.
        """ # noqa: E501

        return self.get_execution_logs_raw(**locals()).data

    @validate_call
    def get_execution_logs_raw(
        self,
        dataset_id: StrictStr,
        project_id: StrictStr,
        force_live: Annotated[Optional[StrictBool], Field(description="force retrieving this info from the executor")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> ApiResponse[GetExecutionLogsResponse]:
        """Get execution logs

        Gets live logs from main execution task

        :param dataset_id: (required)
        :type dataset_id: str
        :param project_id: (required)
        :type project_id: str
        :param force_live: force retrieving this info from the executor
        :type force_live: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_execution_logs_serialize(
            dataset_id=dataset_id,
            project_id=project_id,
            force_live=force_live,
            _headers=_headers,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetExecutionLogsResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    def _get_execution_logs_serialize(
        self,
        dataset_id,
        project_id,
        force_live,
        _headers,
    ) -> RequestSerialized:
        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if dataset_id is not None:
            _path_params['datasetId'] = dataset_id
        if project_id is not None:
            _path_params['projectId'] = project_id
        # process the query parameters
        if force_live is not None:
            
            _query_params.append(('forceLive', force_live))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        # authentication setting
        _auth_settings: List[str] = [
            'accessToken'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/projects/{projectId}/execution/{datasetId}/logs',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats
        )

    @validate_call
    def get_project_summary(
        self,
        project_id: StrictStr,
        number_of_days: Annotated[Optional[StrictInt], Field(description="Number of days of job history to pull")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> Dict[str, List[Task]]:
        """Get execution summary

        Gets an overview of the executions currently running in the project

        :param project_id: (required)
        :type project_id: str
        :param number_of_days: Number of days of job history to pull
        :type number_of_days: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :return: Returns the result object.
        """ # noqa: E501

        return self.get_project_summary_raw(**locals()).data

    @validate_call
    def get_project_summary_raw(
        self,
        project_id: StrictStr,
        number_of_days: Annotated[Optional[StrictInt], Field(description="Number of days of job history to pull")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> ApiResponse[Dict[str, List[Task]]]:
        """Get execution summary

        Gets an overview of the executions currently running in the project

        :param project_id: (required)
        :type project_id: str
        :param number_of_days: Number of days of job history to pull
        :type number_of_days: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_project_summary_serialize(
            project_id=project_id,
            number_of_days=number_of_days,
            _headers=_headers,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Dict[str, List[Task]]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    def _get_project_summary_serialize(
        self,
        project_id,
        number_of_days,
        _headers,
    ) -> RequestSerialized:
        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if project_id is not None:
            _path_params['projectId'] = project_id
        # process the query parameters
        if number_of_days is not None:
            
            _query_params.append(('numberOfDays', number_of_days))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        # authentication setting
        _auth_settings: List[str] = [
            'accessToken'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/projects/{projectId}/execution',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats
        )

    @validate_call
    def get_task_logs(
        self,
        dataset_id: StrictStr,
        project_id: StrictStr,
        task_id: StrictStr,
        force_live: Annotated[Optional[StrictBool], Field(description="force retrieving this info from the executor")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> GetExecutionLogsResponse:
        """Get task logs

        Gets the log output from an individual task

        :param dataset_id: (required)
        :type dataset_id: str
        :param project_id: (required)
        :type project_id: str
        :param task_id: (required)
        :type task_id: str
        :param force_live: force retrieving this info from the executor
        :type force_live: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :return: Returns the result object.
        """ # noqa: E501

        return self.get_task_logs_raw(**locals()).data

    @validate_call
    def get_task_logs_raw(
        self,
        dataset_id: StrictStr,
        project_id: StrictStr,
        task_id: StrictStr,
        force_live: Annotated[Optional[StrictBool], Field(description="force retrieving this info from the executor")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> ApiResponse[GetExecutionLogsResponse]:
        """Get task logs

        Gets the log output from an individual task

        :param dataset_id: (required)
        :type dataset_id: str
        :param project_id: (required)
        :type project_id: str
        :param task_id: (required)
        :type task_id: str
        :param force_live: force retrieving this info from the executor
        :type force_live: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_task_logs_serialize(
            dataset_id=dataset_id,
            project_id=project_id,
            task_id=task_id,
            force_live=force_live,
            _headers=_headers,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetExecutionLogsResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    def _get_task_logs_serialize(
        self,
        dataset_id,
        project_id,
        task_id,
        force_live,
        _headers,
    ) -> RequestSerialized:
        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if dataset_id is not None:
            _path_params['datasetId'] = dataset_id
        if project_id is not None:
            _path_params['projectId'] = project_id
        if task_id is not None:
            _path_params['taskId'] = task_id
        # process the query parameters
        if force_live is not None:
            
            _query_params.append(('forceLive', force_live))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        # authentication setting
        _auth_settings: List[str] = [
            'accessToken'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/projects/{projectId}/execution/{datasetId}/tasks/{taskId}/logs',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats
        )

    @validate_call
    def get_tasks_for_execution(
        self,
        dataset_id: StrictStr,
        project_id: StrictStr,
        force_live: Annotated[Optional[StrictBool], Field(description="force retrieving this info from the executor")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> List[Task]:
        """Get execution tasks

        Gets the tasks submitted by the workflow execution

        :param dataset_id: (required)
        :type dataset_id: str
        :param project_id: (required)
        :type project_id: str
        :param force_live: force retrieving this info from the executor
        :type force_live: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :return: Returns the result object.
        """ # noqa: E501

        return self.get_tasks_for_execution_raw(**locals()).data

    @validate_call
    def get_tasks_for_execution_raw(
        self,
        dataset_id: StrictStr,
        project_id: StrictStr,
        force_live: Annotated[Optional[StrictBool], Field(description="force retrieving this info from the executor")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> ApiResponse[List[Task]]:
        """Get execution tasks

        Gets the tasks submitted by the workflow execution

        :param dataset_id: (required)
        :type dataset_id: str
        :param project_id: (required)
        :type project_id: str
        :param force_live: force retrieving this info from the executor
        :type force_live: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_tasks_for_execution_serialize(
            dataset_id=dataset_id,
            project_id=project_id,
            force_live=force_live,
            _headers=_headers,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Task]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    def _get_tasks_for_execution_serialize(
        self,
        dataset_id,
        project_id,
        force_live,
        _headers,
    ) -> RequestSerialized:
        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if dataset_id is not None:
            _path_params['datasetId'] = dataset_id
        if project_id is not None:
            _path_params['projectId'] = project_id
        # process the query parameters
        if force_live is not None:
            
            _query_params.append(('forceLive', force_live))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        # authentication setting
        _auth_settings: List[str] = [
            'accessToken'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/projects/{projectId}/execution/{datasetId}/tasks',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats
        )

    @validate_call
    def run_analysis(
        self,
        project_id: StrictStr,
        run_analysis_request: RunAnalysisRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> CreateResponse:
        """Run analysis

        Run analysis

        :param project_id: (required)
        :type project_id: str
        :param run_analysis_request: (required)
        :type run_analysis_request: RunAnalysisRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :return: Returns the result object.
        """ # noqa: E501

        return self.run_analysis_raw(**locals()).data

    @validate_call
    def run_analysis_raw(
        self,
        project_id: StrictStr,
        run_analysis_request: RunAnalysisRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> ApiResponse[CreateResponse]:
        """Run analysis

        Run analysis

        :param project_id: (required)
        :type project_id: str
        :param run_analysis_request: (required)
        :type run_analysis_request: RunAnalysisRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._run_analysis_serialize(
            project_id=project_id,
            run_analysis_request=run_analysis_request,
            _headers=_headers,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "CreateResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    def _run_analysis_serialize(
        self,
        project_id,
        run_analysis_request,
        _headers,
    ) -> RequestSerialized:
        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if project_id is not None:
            _path_params['projectId'] = project_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if run_analysis_request is not None:
            _body_params = run_analysis_request

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )
        # set the HTTP header `Content-Type`
        _default_content_type = (
            self.api_client.select_header_content_type(
                [
                    'application/json'
                ]
            )
        )
        if _default_content_type is not None:
            _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'accessToken'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/projects/{projectId}/execution',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats
        )

    @validate_call
    def stop_analysis(
        self,
        dataset_id: StrictStr,
        project_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> StopExecutionResponse:
        """Stop execution

        Terminates all analysis jobs related to this execution

        :param dataset_id: (required)
        :type dataset_id: str
        :param project_id: (required)
        :type project_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :return: Returns the result object.
        """ # noqa: E501

        return self.stop_analysis_raw(**locals()).data

    @validate_call
    def stop_analysis_raw(
        self,
        dataset_id: StrictStr,
        project_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> ApiResponse[StopExecutionResponse]:
        """Stop execution

        Terminates all analysis jobs related to this execution

        :param dataset_id: (required)
        :type dataset_id: str
        :param project_id: (required)
        :type project_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._stop_analysis_serialize(
            dataset_id=dataset_id,
            project_id=project_id,
            _headers=_headers,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StopExecutionResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    def _stop_analysis_serialize(
        self,
        dataset_id,
        project_id,
        _headers,
    ) -> RequestSerialized:
        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if dataset_id is not None:
            _path_params['datasetId'] = dataset_id
        if project_id is not None:
            _path_params['projectId'] = project_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        # authentication setting
        _auth_settings: List[str] = [
            'accessToken'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/projects/{projectId}/execution/{datasetId}/stop',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats
        )
