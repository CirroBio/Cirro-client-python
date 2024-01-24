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

from pydantic import StrictStr

from cirro_api_client.models.aws_credentials import AWSCredentials
from cirro_api_client.models.file_access_request import FileAccessRequest
from cirro_api_client.models.generate_sftp_credentials_request import GenerateSftpCredentialsRequest
from cirro_api_client.models.sftp_credentials import SftpCredentials

from cirro_api_client.api_client import ApiClient, RequestSerialized
from cirro_api_client.api_response import ApiResponse


class FileApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self._api_client = api_client

    @validate_call
    def generate_project_file_access_token(
        self,
        project_id: StrictStr,
        file_access_request: FileAccessRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> AWSCredentials:
        """Create project file access token

        Generates credentials used for connecting via S3

        :param project_id: (required)
        :type project_id: str
        :param file_access_request: (required)
        :type file_access_request: FileAccessRequest
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

        return self.generate_project_file_access_token_raw(
            project_id=project_id,
            file_access_request=file_access_request,
            _request_timeout=_request_timeout,
            _headers=_headers
        ).data

    @validate_call
    def generate_project_file_access_token_raw(
        self,
        project_id: StrictStr,
        file_access_request: FileAccessRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> ApiResponse[AWSCredentials]:
        """Create project file access token

        Generates credentials used for connecting via S3

        :param project_id: (required)
        :type project_id: str
        :param file_access_request: (required)
        :type file_access_request: FileAccessRequest
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

        _param = self._generate_project_file_access_token_serialize(
            project_id=project_id,
            file_access_request=file_access_request,
            _headers=_headers,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AWSCredentials",
        }
        response_data = self._api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self._api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    def _generate_project_file_access_token_serialize(
        self,
        project_id,
        file_access_request,
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
        if file_access_request is not None:
            _body_params = file_access_request

        # set the HTTP header `Accept`
        _header_params['Accept'] = self._api_client.select_header_accept(
            [
                'application/json'
            ]
        )
        # set the HTTP header `Content-Type`
        _default_content_type = (
            self._api_client.select_header_content_type(
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

        return self._api_client.param_serialize(
            method='POST',
            resource_path='/projects/{projectId}/s3-token',
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
    def generate_project_sftp_token(
        self,
        project_id: StrictStr,
        generate_sftp_credentials_request: GenerateSftpCredentialsRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> SftpCredentials:
        """Create project SFTP Token

        Generates credentials used for connecting via SFTP

        :param project_id: (required)
        :type project_id: str
        :param generate_sftp_credentials_request: (required)
        :type generate_sftp_credentials_request: GenerateSftpCredentialsRequest
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

        return self.generate_project_sftp_token_raw(
            project_id=project_id,
            generate_sftp_credentials_request=generate_sftp_credentials_request,
            _request_timeout=_request_timeout,
            _headers=_headers
        ).data

    @validate_call
    def generate_project_sftp_token_raw(
        self,
        project_id: StrictStr,
        generate_sftp_credentials_request: GenerateSftpCredentialsRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> ApiResponse[SftpCredentials]:
        """Create project SFTP Token

        Generates credentials used for connecting via SFTP

        :param project_id: (required)
        :type project_id: str
        :param generate_sftp_credentials_request: (required)
        :type generate_sftp_credentials_request: GenerateSftpCredentialsRequest
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

        _param = self._generate_project_sftp_token_serialize(
            project_id=project_id,
            generate_sftp_credentials_request=generate_sftp_credentials_request,
            _headers=_headers,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SftpCredentials",
        }
        response_data = self._api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self._api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    def _generate_project_sftp_token_serialize(
        self,
        project_id,
        generate_sftp_credentials_request,
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
        if generate_sftp_credentials_request is not None:
            _body_params = generate_sftp_credentials_request

        # set the HTTP header `Accept`
        _header_params['Accept'] = self._api_client.select_header_accept(
            [
                'application/json'
            ]
        )
        # set the HTTP header `Content-Type`
        _default_content_type = (
            self._api_client.select_header_content_type(
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

        return self._api_client.param_serialize(
            method='POST',
            resource_path='/projects/{projectId}/sftp-token',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats
        )
