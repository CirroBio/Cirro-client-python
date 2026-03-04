from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...models.app_registration_detail import AppRegistrationDetail
from ...models.app_registration_input import AppRegistrationInput
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: AppRegistrationInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/app-registrations/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> AppRegistrationDetail | None:
    if response.status_code == 200:
        response_200 = AppRegistrationDetail.from_dict(response.json())

        return response_200

    errors.handle_error_response(response, client.raise_on_unexpected_status)


def _build_response(*, client: Client, response: httpx.Response) -> Response[AppRegistrationDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    body: AppRegistrationInput,
) -> Response[AppRegistrationDetail]:
    """Update app registration

     Updates an existing app registration.

    Args:
        id (str):
        body (AppRegistrationInput):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppRegistrationDetail]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Client,
    body: AppRegistrationInput,
) -> AppRegistrationDetail | None:
    """Update app registration

     Updates an existing app registration.

    Args:
        id (str):
        body (AppRegistrationInput):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppRegistrationDetail
    """

    try:
        return sync_detailed(
            id=id,
            client=client,
            body=body,
        ).parsed
    except errors.NotFoundException:
        return None


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    body: AppRegistrationInput,
) -> Response[AppRegistrationDetail]:
    """Update app registration

     Updates an existing app registration.

    Args:
        id (str):
        body (AppRegistrationInput):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppRegistrationDetail]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    body: AppRegistrationInput,
) -> AppRegistrationDetail | None:
    """Update app registration

     Updates an existing app registration.

    Args:
        id (str):
        body (AppRegistrationInput):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppRegistrationDetail
    """

    try:
        return (
            await asyncio_detailed(
                id=id,
                client=client,
                body=body,
            )
        ).parsed
    except errors.NotFoundException:
        return None
