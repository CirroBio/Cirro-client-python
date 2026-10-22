from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...models.entity_type import EntityType
from ...models.target_mapping import TargetMapping
from ...models.target_mapping_input import TargetMappingInput
from ...types import Response


def _get_kwargs(
    project_id: str,
    sheet_id: str,
    target_type: EntityType,
    target_id: str,
    *,
    body: TargetMappingInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/projects/{project_id}/sheets/{sheet_id}/mappings/{target_type}/{target_id}".format(
            project_id=quote(str(project_id), safe=""),
            sheet_id=quote(str(sheet_id), safe=""),
            target_type=quote(str(target_type), safe=""),
            target_id=quote(str(target_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> TargetMapping | None:
    if response.status_code == 200:
        response_200 = TargetMapping.from_dict(response.json())

        return response_200

    errors.handle_error_response(response, client.raise_on_unexpected_status)


def _build_response(*, client: Client, response: httpx.Response) -> Response[TargetMapping]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    sheet_id: str,
    target_type: EntityType,
    target_id: str,
    *,
    client: Client,
    body: TargetMappingInput,
) -> Response[TargetMapping]:
    """Save column mapping

     Creates or replaces the column mapping from a sheet to a target. Get it first to know whether one
    exists.

    Args:
        project_id (str):
        sheet_id (str):
        target_type (EntityType):
        target_id (str):
        body (TargetMappingInput): The full column mapping from a sheet to a target; saving
            replaces whatever was saved before
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TargetMapping]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        sheet_id=sheet_id,
        target_type=target_type,
        target_id=target_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    sheet_id: str,
    target_type: EntityType,
    target_id: str,
    *,
    client: Client,
    body: TargetMappingInput,
) -> TargetMapping | None:
    """Save column mapping

     Creates or replaces the column mapping from a sheet to a target. Get it first to know whether one
    exists.

    Args:
        project_id (str):
        sheet_id (str):
        target_type (EntityType):
        target_id (str):
        body (TargetMappingInput): The full column mapping from a sheet to a target; saving
            replaces whatever was saved before
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TargetMapping
    """

    try:
        return sync_detailed(
            project_id=project_id,
            sheet_id=sheet_id,
            target_type=target_type,
            target_id=target_id,
            client=client,
            body=body,
        ).parsed
    except errors.NotFoundException:
        return None


async def asyncio_detailed(
    project_id: str,
    sheet_id: str,
    target_type: EntityType,
    target_id: str,
    *,
    client: Client,
    body: TargetMappingInput,
) -> Response[TargetMapping]:
    """Save column mapping

     Creates or replaces the column mapping from a sheet to a target. Get it first to know whether one
    exists.

    Args:
        project_id (str):
        sheet_id (str):
        target_type (EntityType):
        target_id (str):
        body (TargetMappingInput): The full column mapping from a sheet to a target; saving
            replaces whatever was saved before
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TargetMapping]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        sheet_id=sheet_id,
        target_type=target_type,
        target_id=target_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    sheet_id: str,
    target_type: EntityType,
    target_id: str,
    *,
    client: Client,
    body: TargetMappingInput,
) -> TargetMapping | None:
    """Save column mapping

     Creates or replaces the column mapping from a sheet to a target. Get it first to know whether one
    exists.

    Args:
        project_id (str):
        sheet_id (str):
        target_type (EntityType):
        target_id (str):
        body (TargetMappingInput): The full column mapping from a sheet to a target; saving
            replaces whatever was saved before
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TargetMapping
    """

    try:
        return (
            await asyncio_detailed(
                project_id=project_id,
                sheet_id=sheet_id,
                target_type=target_type,
                target_id=target_id,
                client=client,
                body=body,
            )
        ).parsed
    except errors.NotFoundException:
        return None
