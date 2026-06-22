from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...models.dashboard import Dashboard
from ...types import Response


def _get_kwargs(
    dashboard_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dashboards/{dashboard_id}".format(
            dashboard_id=quote(str(dashboard_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> Dashboard | None:
    if response.status_code == 200:
        response_200 = Dashboard.from_dict(response.json())

        return response_200

    errors.handle_error_response(response, client.raise_on_unexpected_status)


def _build_response(*, client: Client, response: httpx.Response) -> Response[Dashboard]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dashboard_id: str,
    *,
    client: Client,
) -> Response[Dashboard]:
    """Get dashboard template

     Retrieves a dashboard template by ID

    Args:
        dashboard_id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dashboard]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
    )

    response = client.get_httpx_client().request(
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dashboard_id: str,
    *,
    client: Client,
) -> Dashboard | None:
    """Get dashboard template

     Retrieves a dashboard template by ID

    Args:
        dashboard_id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dashboard
    """

    try:
        return sync_detailed(
            dashboard_id=dashboard_id,
            client=client,
        ).parsed
    except errors.NotFoundException:
        return None


async def asyncio_detailed(
    dashboard_id: str,
    *,
    client: Client,
) -> Response[Dashboard]:
    """Get dashboard template

     Retrieves a dashboard template by ID

    Args:
        dashboard_id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dashboard]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dashboard_id: str,
    *,
    client: Client,
) -> Dashboard | None:
    """Get dashboard template

     Retrieves a dashboard template by ID

    Args:
        dashboard_id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dashboard
    """

    try:
        return (
            await asyncio_detailed(
                dashboard_id=dashboard_id,
                client=client,
            )
        ).parsed
    except errors.NotFoundException:
        return None
