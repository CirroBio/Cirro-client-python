from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...models.error_message import ErrorMessage
from ...models.portal_error_response import PortalErrorResponse
from ...models.process_revision_save_request import ProcessRevisionSaveRequest
from ...models.process_revision_save_response import ProcessRevisionSaveResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    process_id: str,
    *,
    body: ProcessRevisionSaveRequest,
    if_match: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/processes/{process_id}/revisions".format(
            process_id=quote(str(process_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Client, response: httpx.Response
) -> ErrorMessage | PortalErrorResponse | ProcessRevisionSaveResponse | None:
    if response.status_code == 200:
        response_200 = ProcessRevisionSaveResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PortalErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401

    errors.handle_error_response(response, client.raise_on_unexpected_status)


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[ErrorMessage | PortalErrorResponse | ProcessRevisionSaveResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    process_id: str,
    *,
    client: Client,
    body: ProcessRevisionSaveRequest,
    if_match: None | str | Unset = UNSET,
) -> Response[ErrorMessage | PortalErrorResponse | ProcessRevisionSaveResponse]:
    """Save one or more process configuration resources to storage as a new revision

     Writes the given configuration files to tenant storage and appends a single revision entry that
    records every resource type touched by this save.

    Args:
        process_id (str):
        if_match (None | str | Unset):
        body (ProcessRevisionSaveRequest):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | PortalErrorResponse | ProcessRevisionSaveResponse]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
        body=body,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    process_id: str,
    *,
    client: Client,
    body: ProcessRevisionSaveRequest,
    if_match: None | str | Unset = UNSET,
) -> ErrorMessage | PortalErrorResponse | ProcessRevisionSaveResponse | None:
    """Save one or more process configuration resources to storage as a new revision

     Writes the given configuration files to tenant storage and appends a single revision entry that
    records every resource type touched by this save.

    Args:
        process_id (str):
        if_match (None | str | Unset):
        body (ProcessRevisionSaveRequest):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | PortalErrorResponse | ProcessRevisionSaveResponse
    """

    try:
        return sync_detailed(
            process_id=process_id,
            client=client,
            body=body,
            if_match=if_match,
        ).parsed
    except errors.NotFoundException:
        return None


async def asyncio_detailed(
    process_id: str,
    *,
    client: Client,
    body: ProcessRevisionSaveRequest,
    if_match: None | str | Unset = UNSET,
) -> Response[ErrorMessage | PortalErrorResponse | ProcessRevisionSaveResponse]:
    """Save one or more process configuration resources to storage as a new revision

     Writes the given configuration files to tenant storage and appends a single revision entry that
    records every resource type touched by this save.

    Args:
        process_id (str):
        if_match (None | str | Unset):
        body (ProcessRevisionSaveRequest):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | PortalErrorResponse | ProcessRevisionSaveResponse]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
        body=body,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    process_id: str,
    *,
    client: Client,
    body: ProcessRevisionSaveRequest,
    if_match: None | str | Unset = UNSET,
) -> ErrorMessage | PortalErrorResponse | ProcessRevisionSaveResponse | None:
    """Save one or more process configuration resources to storage as a new revision

     Writes the given configuration files to tenant storage and appends a single revision entry that
    records every resource type touched by this save.

    Args:
        process_id (str):
        if_match (None | str | Unset):
        body (ProcessRevisionSaveRequest):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | PortalErrorResponse | ProcessRevisionSaveResponse
    """

    try:
        return (
            await asyncio_detailed(
                process_id=process_id,
                client=client,
                body=body,
                if_match=if_match,
            )
        ).parsed
    except errors.NotFoundException:
        return None
