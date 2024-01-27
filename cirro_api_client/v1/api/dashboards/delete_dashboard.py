from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dashboard import Dashboard
from ...types import Response


def _get_kwargs(
    project_id: str,
    dashboard_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/projects/{project_id}/dashboards/{dashboard_id}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Dashboard]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Dashboard.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Dashboard]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    dashboard_id: str,
    *,
    client: Client,
) -> Response[Dashboard]:
    """Delete dashboard

     Deletes a dashboard

    Args:
        project_id (str):
        dashboard_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dashboard]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        dashboard_id=dashboard_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    dashboard_id: str,
    *,
    client: Client,
) -> Optional[Dashboard]:
    """Delete dashboard

     Deletes a dashboard

    Args:
        project_id (str):
        dashboard_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dashboard
    """

    return sync_detailed(
        project_id=project_id,
        dashboard_id=dashboard_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    dashboard_id: str,
    *,
    client: Client,
) -> Response[Dashboard]:
    """Delete dashboard

     Deletes a dashboard

    Args:
        project_id (str):
        dashboard_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dashboard]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        dashboard_id=dashboard_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    dashboard_id: str,
    *,
    client: Client,
) -> Optional[Dashboard]:
    """Delete dashboard

     Deletes a dashboard

    Args:
        project_id (str):
        dashboard_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dashboard
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            dashboard_id=dashboard_id,
            client=client,
        )
    ).parsed
