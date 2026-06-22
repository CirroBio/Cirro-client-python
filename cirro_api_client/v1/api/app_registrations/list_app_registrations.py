from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import Client
from ...models.paginated_response_app_registration_dto import PaginatedResponseAppRegistrationDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 100,
    next_token: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["nextToken"] = next_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/app-registrations",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> PaginatedResponseAppRegistrationDto | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseAppRegistrationDto.from_dict(response.json())

        return response_200

    errors.handle_error_response(response, client.raise_on_unexpected_status)


def _build_response(*, client: Client, response: httpx.Response) -> Response[PaginatedResponseAppRegistrationDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    limit: int | Unset = 100,
    next_token: str | Unset = UNSET,
) -> Response[PaginatedResponseAppRegistrationDto]:
    """List app registrations

     Lists all app registrations in the system.

    Args:
        limit (int | Unset):  Default: 100.
        next_token (str | Unset):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseAppRegistrationDto]
    """

    kwargs = _get_kwargs(
        limit=limit,
        next_token=next_token,
    )

    response = client.get_httpx_client().request(
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    limit: int | Unset = 100,
    next_token: str | Unset = UNSET,
) -> PaginatedResponseAppRegistrationDto | None:
    """List app registrations

     Lists all app registrations in the system.

    Args:
        limit (int | Unset):  Default: 100.
        next_token (str | Unset):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseAppRegistrationDto
    """

    try:
        return sync_detailed(
            client=client,
            limit=limit,
            next_token=next_token,
        ).parsed
    except errors.NotFoundException:
        return None


async def asyncio_detailed(
    *,
    client: Client,
    limit: int | Unset = 100,
    next_token: str | Unset = UNSET,
) -> Response[PaginatedResponseAppRegistrationDto]:
    """List app registrations

     Lists all app registrations in the system.

    Args:
        limit (int | Unset):  Default: 100.
        next_token (str | Unset):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseAppRegistrationDto]
    """

    kwargs = _get_kwargs(
        limit=limit,
        next_token=next_token,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    limit: int | Unset = 100,
    next_token: str | Unset = UNSET,
) -> PaginatedResponseAppRegistrationDto | None:
    """List app registrations

     Lists all app registrations in the system.

    Args:
        limit (int | Unset):  Default: 100.
        next_token (str | Unset):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseAppRegistrationDto
    """

    try:
        return (
            await asyncio_detailed(
                client=client,
                limit=limit,
                next_token=next_token,
            )
        ).parsed
    except errors.NotFoundException:
        return None
