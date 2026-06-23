from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...models.error_message import ErrorMessage
from ...models.paginated_response_process_revision_dto import PaginatedResponseProcessRevisionDto
from ...models.portal_error_response import PortalErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    process_id: str,
    *,
    limit: int | Unset = 20,
    next_token: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["nextToken"] = next_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/processes/{process_id}/revisions".format(
            process_id=quote(str(process_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Client, response: httpx.Response
) -> ErrorMessage | PaginatedResponseProcessRevisionDto | PortalErrorResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseProcessRevisionDto.from_dict(response.json())

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
) -> Response[ErrorMessage | PaginatedResponseProcessRevisionDto | PortalErrorResponse]:
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
    limit: int | Unset = 20,
    next_token: str | Unset = UNSET,
) -> Response[ErrorMessage | PaginatedResponseProcessRevisionDto | PortalErrorResponse]:
    """List configuration revisions for a process that are in storage

     Paginated, newest-first by default. Returns 404 for processes without configuration in tenant
    storage

    Args:
        process_id (str):
        limit (int | Unset):  Default: 20.
        next_token (str | Unset):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | PaginatedResponseProcessRevisionDto | PortalErrorResponse]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
        limit=limit,
        next_token=next_token,
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
    limit: int | Unset = 20,
    next_token: str | Unset = UNSET,
) -> ErrorMessage | PaginatedResponseProcessRevisionDto | PortalErrorResponse | None:
    """List configuration revisions for a process that are in storage

     Paginated, newest-first by default. Returns 404 for processes without configuration in tenant
    storage

    Args:
        process_id (str):
        limit (int | Unset):  Default: 20.
        next_token (str | Unset):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | PaginatedResponseProcessRevisionDto | PortalErrorResponse
    """

    try:
        return sync_detailed(
            process_id=process_id,
            client=client,
            limit=limit,
            next_token=next_token,
        ).parsed
    except errors.NotFoundException:
        return None


async def asyncio_detailed(
    process_id: str,
    *,
    client: Client,
    limit: int | Unset = 20,
    next_token: str | Unset = UNSET,
) -> Response[ErrorMessage | PaginatedResponseProcessRevisionDto | PortalErrorResponse]:
    """List configuration revisions for a process that are in storage

     Paginated, newest-first by default. Returns 404 for processes without configuration in tenant
    storage

    Args:
        process_id (str):
        limit (int | Unset):  Default: 20.
        next_token (str | Unset):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | PaginatedResponseProcessRevisionDto | PortalErrorResponse]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
        limit=limit,
        next_token=next_token,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    process_id: str,
    *,
    client: Client,
    limit: int | Unset = 20,
    next_token: str | Unset = UNSET,
) -> ErrorMessage | PaginatedResponseProcessRevisionDto | PortalErrorResponse | None:
    """List configuration revisions for a process that are in storage

     Paginated, newest-first by default. Returns 404 for processes without configuration in tenant
    storage

    Args:
        process_id (str):
        limit (int | Unset):  Default: 20.
        next_token (str | Unset):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | PaginatedResponseProcessRevisionDto | PortalErrorResponse
    """

    try:
        return (
            await asyncio_detailed(
                process_id=process_id,
                client=client,
                limit=limit,
                next_token=next_token,
            )
        ).parsed
    except errors.NotFoundException:
        return None
