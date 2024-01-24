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
from pydantic import StrictBool, StrictStr

from typing import List, Optional

from cirro_api_client.models.billing_account import BillingAccount
from cirro_api_client.models.billing_account_request import BillingAccountRequest
from cirro_api_client.models.create_response import CreateResponse

from cirro_api_client.api_client import ApiClient, RequestSerialized
from cirro_api_client.api_response import ApiResponse


class BillingApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self._api_client = api_client

    @validate_call
    def create_billing_account(
        self,
        billing_account_request: BillingAccountRequest,
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
        """Create billing account

        Creates a billing account

        :param billing_account_request: (required)
        :type billing_account_request: BillingAccountRequest
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

        return self.create_billing_account_raw(
            billing_account_request=billing_account_request,
            _request_timeout=_request_timeout,
            _headers=_headers
        ).data

    @validate_call
    def create_billing_account_raw(
        self,
        billing_account_request: BillingAccountRequest,
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
        """Create billing account

        Creates a billing account

        :param billing_account_request: (required)
        :type billing_account_request: BillingAccountRequest
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

        _param = self._create_billing_account_serialize(
            billing_account_request=billing_account_request,
            _headers=_headers,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "CreateResponse",
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

    def _create_billing_account_serialize(
        self,
        billing_account_request,
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
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if billing_account_request is not None:
            _body_params = billing_account_request

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
            resource_path='/billing',
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
    def delete_billing_account(
        self,
        billing_account_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> None:
        """Delete billing account

        Deletes a billing account

        :param billing_account_id: (required)
        :type billing_account_id: str
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

        return self.delete_billing_account_raw(
            billing_account_id=billing_account_id,
            _request_timeout=_request_timeout,
            _headers=_headers
        ).data

    @validate_call
    def delete_billing_account_raw(
        self,
        billing_account_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> ApiResponse[None]:
        """Delete billing account

        Deletes a billing account

        :param billing_account_id: (required)
        :type billing_account_id: str
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

        _param = self._delete_billing_account_serialize(
            billing_account_id=billing_account_id,
            _headers=_headers,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
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

    def _delete_billing_account_serialize(
        self,
        billing_account_id,
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
        if billing_account_id is not None:
            _path_params['billingAccountId'] = billing_account_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter



        # authentication setting
        _auth_settings: List[str] = [
            'accessToken'
        ]

        return self._api_client.param_serialize(
            method='DELETE',
            resource_path='/billing/{billingAccountId}',
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
    def generate_billing_report(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> None:
        """Generate billing report

        Generates a billing report xlsx with cost information

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

        return self.generate_billing_report_raw(
            _request_timeout=_request_timeout,
            _headers=_headers
        ).data

    @validate_call
    def generate_billing_report_raw(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> ApiResponse[None]:
        """Generate billing report

        Generates a billing report xlsx with cost information

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

        _param = self._generate_billing_report_serialize(
            _headers=_headers,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
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

    def _generate_billing_report_serialize(
        self,
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
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        _header_params['Accept'] = self._api_client.select_header_accept(
            [
                'application/vnd.ms-excel'
            ]
        )

        # authentication setting
        _auth_settings: List[str] = [
            'accessToken'
        ]

        return self._api_client.param_serialize(
            method='GET',
            resource_path='/billing-report',
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
    def get_billing_accounts(
        self,
        include_archived: Annotated[Optional[StrictBool], Field(description="Include billing accounts that are no longer in use")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> List[BillingAccount]:
        """List billing accounts

        Gets a list of billing accounts the current user has access to

        :param include_archived: Include billing accounts that are no longer in use
        :type include_archived: bool
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

        return self.get_billing_accounts_raw(
            include_archived=include_archived,
            _request_timeout=_request_timeout,
            _headers=_headers
        ).data

    @validate_call
    def get_billing_accounts_raw(
        self,
        include_archived: Annotated[Optional[StrictBool], Field(description="Include billing accounts that are no longer in use")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> ApiResponse[List[BillingAccount]]:
        """List billing accounts

        Gets a list of billing accounts the current user has access to

        :param include_archived: Include billing accounts that are no longer in use
        :type include_archived: bool
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

        _param = self._get_billing_accounts_serialize(
            include_archived=include_archived,
            _headers=_headers,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[BillingAccount]",
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

    def _get_billing_accounts_serialize(
        self,
        include_archived,
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
        # process the query parameters
        if include_archived is not None:
            
            _query_params.append(('includeArchived', include_archived))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        _header_params['Accept'] = self._api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        # authentication setting
        _auth_settings: List[str] = [
            'accessToken'
        ]

        return self._api_client.param_serialize(
            method='GET',
            resource_path='/billing',
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
    def update_billing_account(
        self,
        billing_account_id: StrictStr,
        billing_account_request: BillingAccountRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> None:
        """Update billing account

        Updates a billing account

        :param billing_account_id: (required)
        :type billing_account_id: str
        :param billing_account_request: (required)
        :type billing_account_request: BillingAccountRequest
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

        return self.update_billing_account_raw(
            billing_account_id=billing_account_id,
            billing_account_request=billing_account_request,
            _request_timeout=_request_timeout,
            _headers=_headers
        ).data

    @validate_call
    def update_billing_account_raw(
        self,
        billing_account_id: StrictStr,
        billing_account_request: BillingAccountRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
    ) -> ApiResponse[None]:
        """Update billing account

        Updates a billing account

        :param billing_account_id: (required)
        :type billing_account_id: str
        :param billing_account_request: (required)
        :type billing_account_request: BillingAccountRequest
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

        _param = self._update_billing_account_serialize(
            billing_account_id=billing_account_id,
            billing_account_request=billing_account_request,
            _headers=_headers,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
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

    def _update_billing_account_serialize(
        self,
        billing_account_id,
        billing_account_request,
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
        if billing_account_id is not None:
            _path_params['billingAccountId'] = billing_account_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if billing_account_request is not None:
            _body_params = billing_account_request


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
            method='PUT',
            resource_path='/billing/{billingAccountId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats
        )
