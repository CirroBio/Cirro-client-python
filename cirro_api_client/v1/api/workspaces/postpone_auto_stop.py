from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import Client
from ...models.postpone_workspace_autostop_input import PostponeWorkspaceAutostopInput
from ...models.workspace import Workspace
from ...types import Response


def _get_kwargs(
    project_id: str,
    workspace_id: str,
    *,
    body: PostponeWorkspaceAutostopInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/workspaces/{workspace_id}:postpone-auto-stop",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> Workspace | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = Workspace.from_dict(response.json())

        return response_200

    errors.handle_error_response(response, client.raise_on_unexpected_status)


def _build_response(*, client: Client, response: httpx.Response) -> Response[Workspace]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    workspace_id: str,
    *,
    client: Client,
    body: PostponeWorkspaceAutostopInput,
) -> Response[Workspace]:
    """Postpone workspace autostop

     Postpone autostop for the given workspace

    Args:
        project_id (str):
        workspace_id (str):
        body (PostponeWorkspaceAutostopInput):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Workspace]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        workspace_id=workspace_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    workspace_id: str,
    *,
    client: Client,
    body: PostponeWorkspaceAutostopInput,
) -> Workspace | None:
    """Postpone workspace autostop

     Postpone autostop for the given workspace

    Args:
        project_id (str):
        workspace_id (str):
        body (PostponeWorkspaceAutostopInput):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Workspace
    """

    try:
        return sync_detailed(
            project_id=project_id,
            workspace_id=workspace_id,
            client=client,
            body=body,
        ).parsed
    except errors.NotFoundException:
        return None


async def asyncio_detailed(
    project_id: str,
    workspace_id: str,
    *,
    client: Client,
    body: PostponeWorkspaceAutostopInput,
) -> Response[Workspace]:
    """Postpone workspace autostop

     Postpone autostop for the given workspace

    Args:
        project_id (str):
        workspace_id (str):
        body (PostponeWorkspaceAutostopInput):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Workspace]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        workspace_id=workspace_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    workspace_id: str,
    *,
    client: Client,
    body: PostponeWorkspaceAutostopInput,
) -> Workspace | None:
    """Postpone workspace autostop

     Postpone autostop for the given workspace

    Args:
        project_id (str):
        workspace_id (str):
        body (PostponeWorkspaceAutostopInput):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Workspace
    """

    try:
        return (
            await asyncio_detailed(
                project_id=project_id,
                workspace_id=workspace_id,
                client=client,
                body=body,
            )
        ).parsed
    except errors.NotFoundException:
        return None
