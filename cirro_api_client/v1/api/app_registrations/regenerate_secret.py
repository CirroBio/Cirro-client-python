from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...models.app_registration_secret_response import AppRegistrationSecretResponse
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/app-registrations/{id}:regenerate-secret".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> AppRegistrationSecretResponse | None:
    if response.status_code == 200:
        response_200 = AppRegistrationSecretResponse.from_dict(response.json())

        return response_200

    errors.handle_error_response(response, client.raise_on_unexpected_status)


def _build_response(*, client: Client, response: httpx.Response) -> Response[AppRegistrationSecretResponse]:
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
) -> Response[AppRegistrationSecretResponse]:
    """Regenerate client secret

     Generates a new client secret for the app registration. The old secret is invalidated.

    Args:
        id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppRegistrationSecretResponse]
    """

    kwargs = _get_kwargs(
        id=id,
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
) -> AppRegistrationSecretResponse | None:
    """Regenerate client secret

     Generates a new client secret for the app registration. The old secret is invalidated.

    Args:
        id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppRegistrationSecretResponse
    """

    try:
        return sync_detailed(
            id=id,
            client=client,
        ).parsed
    except errors.NotFoundException:
        return None


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
) -> Response[AppRegistrationSecretResponse]:
    """Regenerate client secret

     Generates a new client secret for the app registration. The old secret is invalidated.

    Args:
        id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppRegistrationSecretResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
) -> AppRegistrationSecretResponse | None:
    """Regenerate client secret

     Generates a new client secret for the app registration. The old secret is invalidated.

    Args:
        id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppRegistrationSecretResponse
    """

    try:
        return (
            await asyncio_detailed(
                id=id,
                client=client,
            )
        ).parsed
    except errors.NotFoundException:
        return None
