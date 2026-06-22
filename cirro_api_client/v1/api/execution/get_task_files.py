from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...models.get_task_files_response import GetTaskFilesResponse
from ...types import Response


def _get_kwargs(
    project_id: str,
    dataset_id: str,
    task_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/execution/{dataset_id}/tasks/{task_id}/files".format(
            project_id=quote(str(project_id), safe=""),
            dataset_id=quote(str(dataset_id), safe=""),
            task_id=quote(str(task_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> GetTaskFilesResponse | None:
    if response.status_code == 200:
        response_200 = GetTaskFilesResponse.from_dict(response.json())

        return response_200

    errors.handle_error_response(response, client.raise_on_unexpected_status)


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetTaskFilesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    dataset_id: str,
    task_id: str,
    *,
    client: Client,
) -> Response[GetTaskFilesResponse]:
    """Get task files

     Gets the input and output files for an individual Nextflow task

    Args:
        project_id (str):
        dataset_id (str):
        task_id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTaskFilesResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        dataset_id=dataset_id,
        task_id=task_id,
    )

    response = client.get_httpx_client().request(
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    dataset_id: str,
    task_id: str,
    *,
    client: Client,
) -> GetTaskFilesResponse | None:
    """Get task files

     Gets the input and output files for an individual Nextflow task

    Args:
        project_id (str):
        dataset_id (str):
        task_id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTaskFilesResponse
    """

    try:
        return sync_detailed(
            project_id=project_id,
            dataset_id=dataset_id,
            task_id=task_id,
            client=client,
        ).parsed
    except errors.NotFoundException:
        return None


async def asyncio_detailed(
    project_id: str,
    dataset_id: str,
    task_id: str,
    *,
    client: Client,
) -> Response[GetTaskFilesResponse]:
    """Get task files

     Gets the input and output files for an individual Nextflow task

    Args:
        project_id (str):
        dataset_id (str):
        task_id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTaskFilesResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        dataset_id=dataset_id,
        task_id=task_id,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    dataset_id: str,
    task_id: str,
    *,
    client: Client,
) -> GetTaskFilesResponse | None:
    """Get task files

     Gets the input and output files for an individual Nextflow task

    Args:
        project_id (str):
        dataset_id (str):
        task_id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTaskFilesResponse
    """

    try:
        return (
            await asyncio_detailed(
                project_id=project_id,
                dataset_id=dataset_id,
                task_id=task_id,
                client=client,
            )
        ).parsed
    except errors.NotFoundException:
        return None
