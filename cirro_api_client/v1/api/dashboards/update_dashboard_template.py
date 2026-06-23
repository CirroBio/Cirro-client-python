from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...models.dashboard import Dashboard
from ...models.dashboard_input import DashboardInput
from ...types import Response


def _get_kwargs(
    dashboard_id: str,
    *,
    body: DashboardInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/dashboards/{dashboard_id}".format(
            dashboard_id=quote(str(dashboard_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: DashboardInput,
) -> Response[Dashboard]:
    """Update dashboard template

     Updates a dashboard template

    Args:
        dashboard_id (str):
        body (DashboardInput):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dashboard]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
        body=body,
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
    body: DashboardInput,
) -> Dashboard | None:
    """Update dashboard template

     Updates a dashboard template

    Args:
        dashboard_id (str):
        body (DashboardInput):
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
            body=body,
        ).parsed
    except errors.NotFoundException:
        return None


async def asyncio_detailed(
    dashboard_id: str,
    *,
    client: Client,
    body: DashboardInput,
) -> Response[Dashboard]:
    """Update dashboard template

     Updates a dashboard template

    Args:
        dashboard_id (str):
        body (DashboardInput):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dashboard]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dashboard_id: str,
    *,
    client: Client,
    body: DashboardInput,
) -> Dashboard | None:
    """Update dashboard template

     Updates a dashboard template

    Args:
        dashboard_id (str):
        body (DashboardInput):
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
                body=body,
            )
        ).parsed
    except errors.NotFoundException:
        return None
