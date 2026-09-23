import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...models.dataset_source import DatasetSource
from ...models.project_file_query_response import ProjectFileQueryResponse
from ...models.sql_sort_order import SqlSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    source: DatasetSource | None | Unset = UNSET,
    file_type: None | str | Unset = UNSET,
    dataset_id: None | str | Unset = UNSET,
    process_id: None | str | Unset = UNSET,
    created_by: None | str | Unset = UNSET,
    path_contains: None | str | Unset = UNSET,
    min_size: int | None | Unset = UNSET,
    max_size: int | None | Unset = UNSET,
    created_after: datetime.datetime | None | Unset = UNSET,
    created_before: datetime.datetime | None | Unset = UNSET,
    sort_order: None | SqlSortOrder | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    next_token: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_source: None | str | Unset
    if isinstance(source, Unset):
        json_source = UNSET
    elif isinstance(source, DatasetSource):
        json_source = source.value
    else:
        json_source = source
    params["source"] = json_source

    json_file_type: None | str | Unset
    if isinstance(file_type, Unset):
        json_file_type = UNSET
    else:
        json_file_type = file_type
    params["fileType"] = json_file_type

    json_dataset_id: None | str | Unset
    if isinstance(dataset_id, Unset):
        json_dataset_id = UNSET
    else:
        json_dataset_id = dataset_id
    params["datasetId"] = json_dataset_id

    json_process_id: None | str | Unset
    if isinstance(process_id, Unset):
        json_process_id = UNSET
    else:
        json_process_id = process_id
    params["processId"] = json_process_id

    json_created_by: None | str | Unset
    if isinstance(created_by, Unset):
        json_created_by = UNSET
    else:
        json_created_by = created_by
    params["createdBy"] = json_created_by

    json_path_contains: None | str | Unset
    if isinstance(path_contains, Unset):
        json_path_contains = UNSET
    else:
        json_path_contains = path_contains
    params["pathContains"] = json_path_contains

    json_min_size: int | None | Unset
    if isinstance(min_size, Unset):
        json_min_size = UNSET
    else:
        json_min_size = min_size
    params["minSize"] = json_min_size

    json_max_size: int | None | Unset
    if isinstance(max_size, Unset):
        json_max_size = UNSET
    else:
        json_max_size = max_size
    params["maxSize"] = json_max_size

    json_created_after: None | str | Unset
    if isinstance(created_after, Unset):
        json_created_after = UNSET
    elif isinstance(created_after, datetime.datetime):
        json_created_after = created_after.isoformat()
    else:
        json_created_after = created_after
    params["createdAfter"] = json_created_after

    json_created_before: None | str | Unset
    if isinstance(created_before, Unset):
        json_created_before = UNSET
    elif isinstance(created_before, datetime.datetime):
        json_created_before = created_before.isoformat()
    else:
        json_created_before = created_before
    params["createdBefore"] = json_created_before

    json_sort_order: None | str | Unset
    if isinstance(sort_order, Unset):
        json_sort_order = UNSET
    elif isinstance(sort_order, SqlSortOrder):
        json_sort_order = sort_order.value
    else:
        json_sort_order = sort_order
    params["sortOrder"] = json_sort_order

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_next_token: None | str | Unset
    if isinstance(next_token, Unset):
        json_next_token = UNSET
    else:
        json_next_token = next_token
    params["nextToken"] = json_next_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/files".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> ProjectFileQueryResponse | None:
    if response.status_code == 200:
        response_200 = ProjectFileQueryResponse.from_dict(response.json())

        return response_200

    errors.handle_error_response(response, client.raise_on_unexpected_status)


def _build_response(*, client: Client, response: httpx.Response) -> Response[ProjectFileQueryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: Client,
    source: DatasetSource | None | Unset = UNSET,
    file_type: None | str | Unset = UNSET,
    dataset_id: None | str | Unset = UNSET,
    process_id: None | str | Unset = UNSET,
    created_by: None | str | Unset = UNSET,
    path_contains: None | str | Unset = UNSET,
    min_size: int | None | Unset = UNSET,
    max_size: int | None | Unset = UNSET,
    created_after: datetime.datetime | None | Unset = UNSET,
    created_before: datetime.datetime | None | Unset = UNSET,
    sort_order: None | SqlSortOrder | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    next_token: None | str | Unset = UNSET,
) -> Response[ProjectFileQueryResponse]:
    """Search project files

     Queries the project for files, with optional filtering, sorting, and pagination.

    Args:
        project_id (str):
        source (DatasetSource | None | Unset):
        file_type (None | str | Unset):
        dataset_id (None | str | Unset):
        process_id (None | str | Unset):
        created_by (None | str | Unset):
        path_contains (None | str | Unset):
        min_size (int | None | Unset):
        max_size (int | None | Unset):
        created_after (datetime.datetime | None | Unset):
        created_before (datetime.datetime | None | Unset):
        sort_order (None | SqlSortOrder | Unset):
        limit (int | None | Unset):
        next_token (None | str | Unset):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectFileQueryResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        source=source,
        file_type=file_type,
        dataset_id=dataset_id,
        process_id=process_id,
        created_by=created_by,
        path_contains=path_contains,
        min_size=min_size,
        max_size=max_size,
        created_after=created_after,
        created_before=created_before,
        sort_order=sort_order,
        limit=limit,
        next_token=next_token,
    )

    response = client.get_httpx_client().request(
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: Client,
    source: DatasetSource | None | Unset = UNSET,
    file_type: None | str | Unset = UNSET,
    dataset_id: None | str | Unset = UNSET,
    process_id: None | str | Unset = UNSET,
    created_by: None | str | Unset = UNSET,
    path_contains: None | str | Unset = UNSET,
    min_size: int | None | Unset = UNSET,
    max_size: int | None | Unset = UNSET,
    created_after: datetime.datetime | None | Unset = UNSET,
    created_before: datetime.datetime | None | Unset = UNSET,
    sort_order: None | SqlSortOrder | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    next_token: None | str | Unset = UNSET,
) -> ProjectFileQueryResponse | None:
    """Search project files

     Queries the project for files, with optional filtering, sorting, and pagination.

    Args:
        project_id (str):
        source (DatasetSource | None | Unset):
        file_type (None | str | Unset):
        dataset_id (None | str | Unset):
        process_id (None | str | Unset):
        created_by (None | str | Unset):
        path_contains (None | str | Unset):
        min_size (int | None | Unset):
        max_size (int | None | Unset):
        created_after (datetime.datetime | None | Unset):
        created_before (datetime.datetime | None | Unset):
        sort_order (None | SqlSortOrder | Unset):
        limit (int | None | Unset):
        next_token (None | str | Unset):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectFileQueryResponse
    """

    try:
        return sync_detailed(
            project_id=project_id,
            client=client,
            source=source,
            file_type=file_type,
            dataset_id=dataset_id,
            process_id=process_id,
            created_by=created_by,
            path_contains=path_contains,
            min_size=min_size,
            max_size=max_size,
            created_after=created_after,
            created_before=created_before,
            sort_order=sort_order,
            limit=limit,
            next_token=next_token,
        ).parsed
    except errors.NotFoundException:
        return None


async def asyncio_detailed(
    project_id: str,
    *,
    client: Client,
    source: DatasetSource | None | Unset = UNSET,
    file_type: None | str | Unset = UNSET,
    dataset_id: None | str | Unset = UNSET,
    process_id: None | str | Unset = UNSET,
    created_by: None | str | Unset = UNSET,
    path_contains: None | str | Unset = UNSET,
    min_size: int | None | Unset = UNSET,
    max_size: int | None | Unset = UNSET,
    created_after: datetime.datetime | None | Unset = UNSET,
    created_before: datetime.datetime | None | Unset = UNSET,
    sort_order: None | SqlSortOrder | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    next_token: None | str | Unset = UNSET,
) -> Response[ProjectFileQueryResponse]:
    """Search project files

     Queries the project for files, with optional filtering, sorting, and pagination.

    Args:
        project_id (str):
        source (DatasetSource | None | Unset):
        file_type (None | str | Unset):
        dataset_id (None | str | Unset):
        process_id (None | str | Unset):
        created_by (None | str | Unset):
        path_contains (None | str | Unset):
        min_size (int | None | Unset):
        max_size (int | None | Unset):
        created_after (datetime.datetime | None | Unset):
        created_before (datetime.datetime | None | Unset):
        sort_order (None | SqlSortOrder | Unset):
        limit (int | None | Unset):
        next_token (None | str | Unset):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectFileQueryResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        source=source,
        file_type=file_type,
        dataset_id=dataset_id,
        process_id=process_id,
        created_by=created_by,
        path_contains=path_contains,
        min_size=min_size,
        max_size=max_size,
        created_after=created_after,
        created_before=created_before,
        sort_order=sort_order,
        limit=limit,
        next_token=next_token,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: Client,
    source: DatasetSource | None | Unset = UNSET,
    file_type: None | str | Unset = UNSET,
    dataset_id: None | str | Unset = UNSET,
    process_id: None | str | Unset = UNSET,
    created_by: None | str | Unset = UNSET,
    path_contains: None | str | Unset = UNSET,
    min_size: int | None | Unset = UNSET,
    max_size: int | None | Unset = UNSET,
    created_after: datetime.datetime | None | Unset = UNSET,
    created_before: datetime.datetime | None | Unset = UNSET,
    sort_order: None | SqlSortOrder | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    next_token: None | str | Unset = UNSET,
) -> ProjectFileQueryResponse | None:
    """Search project files

     Queries the project for files, with optional filtering, sorting, and pagination.

    Args:
        project_id (str):
        source (DatasetSource | None | Unset):
        file_type (None | str | Unset):
        dataset_id (None | str | Unset):
        process_id (None | str | Unset):
        created_by (None | str | Unset):
        path_contains (None | str | Unset):
        min_size (int | None | Unset):
        max_size (int | None | Unset):
        created_after (datetime.datetime | None | Unset):
        created_before (datetime.datetime | None | Unset):
        sort_order (None | SqlSortOrder | Unset):
        limit (int | None | Unset):
        next_token (None | str | Unset):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectFileQueryResponse
    """

    try:
        return (
            await asyncio_detailed(
                project_id=project_id,
                client=client,
                source=source,
                file_type=file_type,
                dataset_id=dataset_id,
                process_id=process_id,
                created_by=created_by,
                path_contains=path_contains,
                min_size=min_size,
                max_size=max_size,
                created_after=created_after,
                created_before=created_before,
                sort_order=sort_order,
                limit=limit,
                next_token=next_token,
            )
        ).parsed
    except errors.NotFoundException:
        return None
