from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.compute_environment_configuration_input import ComputeEnvironmentConfigurationInput
from ...types import Response


def _get_kwargs(
    project_id: str,
    compute_environment_id: str,
    *,
    body: ComputeEnvironmentConfigurationInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/projects/{project_id}/compute-environments/{compute_environment_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None

    errors.handle_error_response(response, client.raise_on_unexpected_status)


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    compute_environment_id: str,
    *,
    client: Client,
    body: ComputeEnvironmentConfigurationInput,
) -> Response[Any]:
    """Update compute environment

     Update a compute environment for a project

    Args:
        project_id (str):
        compute_environment_id (str):
        body (ComputeEnvironmentConfigurationInput):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        compute_environment_id=compute_environment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id: str,
    compute_environment_id: str,
    *,
    client: Client,
    body: ComputeEnvironmentConfigurationInput,
) -> Response[Any]:
    """Update compute environment

     Update a compute environment for a project

    Args:
        project_id (str):
        compute_environment_id (str):
        body (ComputeEnvironmentConfigurationInput):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        compute_environment_id=compute_environment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)
