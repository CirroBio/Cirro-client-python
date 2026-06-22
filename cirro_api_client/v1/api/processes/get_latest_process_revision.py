from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...models.error_message import ErrorMessage
from ...models.portal_error_response import PortalErrorResponse
from ...models.process_revision_dto import ProcessRevisionDto
from ...types import Response


def _get_kwargs(
    process_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/processes/{process_id}/revisions:latest".format(
            process_id=quote(str(process_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Client, response: httpx.Response
) -> ErrorMessage | PortalErrorResponse | ProcessRevisionDto | None:
    if response.status_code == 200:
        response_200 = ProcessRevisionDto.from_dict(response.json())

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
) -> Response[ErrorMessage | PortalErrorResponse | ProcessRevisionDto]:
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
) -> Response[ErrorMessage | PortalErrorResponse | ProcessRevisionDto]:
    """Fetch the latest configuration revision for a process

     Returns the highest-numbered revision entry for the given process. Returns 404 for processes without
    configuration in tenant storage.

    Args:
        process_id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | PortalErrorResponse | ProcessRevisionDto]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
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
) -> ErrorMessage | PortalErrorResponse | ProcessRevisionDto | None:
    """Fetch the latest configuration revision for a process

     Returns the highest-numbered revision entry for the given process. Returns 404 for processes without
    configuration in tenant storage.

    Args:
        process_id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | PortalErrorResponse | ProcessRevisionDto
    """

    try:
        return sync_detailed(
            process_id=process_id,
            client=client,
        ).parsed
    except errors.NotFoundException:
        return None


async def asyncio_detailed(
    process_id: str,
    *,
    client: Client,
) -> Response[ErrorMessage | PortalErrorResponse | ProcessRevisionDto]:
    """Fetch the latest configuration revision for a process

     Returns the highest-numbered revision entry for the given process. Returns 404 for processes without
    configuration in tenant storage.

    Args:
        process_id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorMessage | PortalErrorResponse | ProcessRevisionDto]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    process_id: str,
    *,
    client: Client,
) -> ErrorMessage | PortalErrorResponse | ProcessRevisionDto | None:
    """Fetch the latest configuration revision for a process

     Returns the highest-numbered revision entry for the given process. Returns 404 for processes without
    configuration in tenant storage.

    Args:
        process_id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorMessage | PortalErrorResponse | ProcessRevisionDto
    """

    try:
        return (
            await asyncio_detailed(
                process_id=process_id,
                client=client,
            )
        ).parsed
    except errors.NotFoundException:
        return None
