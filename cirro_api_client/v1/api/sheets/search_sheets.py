from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...models.sheet_search_response import SheetSearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    value_contains: str,
    limit: int | Unset = 100,
    page: int | Unset = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["valueContains"] = value_contains

    params["limit"] = limit

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/sheets/search".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> SheetSearchResponse | None:
    if response.status_code == 200:
        response_200 = SheetSearchResponse.from_dict(response.json())

        return response_200

    errors.handle_error_response(response, client.raise_on_unexpected_status)


def _build_response(*, client: Client, response: httpx.Response) -> Response[SheetSearchResponse]:
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
    value_contains: str,
    limit: int | Unset = 100,
    page: int | Unset = 1,
) -> Response[SheetSearchResponse]:
    """Search the project's sheets

     Finds values that contain valueContains, ignoring case, in every indexed column of the project's
    TABLE sheets. Returns a page of hits, one per distinct value in a column of a sheet. Each hit's
    rowCount is the number of rows in that sheet with the value in that column.

    Args:
        project_id (str):
        value_contains (str):
        limit (int | Unset):  Default: 100.
        page (int | Unset):  Default: 1.
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SheetSearchResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        value_contains=value_contains,
        limit=limit,
        page=page,
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
    value_contains: str,
    limit: int | Unset = 100,
    page: int | Unset = 1,
) -> SheetSearchResponse | None:
    """Search the project's sheets

     Finds values that contain valueContains, ignoring case, in every indexed column of the project's
    TABLE sheets. Returns a page of hits, one per distinct value in a column of a sheet. Each hit's
    rowCount is the number of rows in that sheet with the value in that column.

    Args:
        project_id (str):
        value_contains (str):
        limit (int | Unset):  Default: 100.
        page (int | Unset):  Default: 1.
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SheetSearchResponse
    """

    try:
        return sync_detailed(
            project_id=project_id,
            client=client,
            value_contains=value_contains,
            limit=limit,
            page=page,
        ).parsed
    except errors.NotFoundException:
        return None


async def asyncio_detailed(
    project_id: str,
    *,
    client: Client,
    value_contains: str,
    limit: int | Unset = 100,
    page: int | Unset = 1,
) -> Response[SheetSearchResponse]:
    """Search the project's sheets

     Finds values that contain valueContains, ignoring case, in every indexed column of the project's
    TABLE sheets. Returns a page of hits, one per distinct value in a column of a sheet. Each hit's
    rowCount is the number of rows in that sheet with the value in that column.

    Args:
        project_id (str):
        value_contains (str):
        limit (int | Unset):  Default: 100.
        page (int | Unset):  Default: 1.
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SheetSearchResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        value_contains=value_contains,
        limit=limit,
        page=page,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: Client,
    value_contains: str,
    limit: int | Unset = 100,
    page: int | Unset = 1,
) -> SheetSearchResponse | None:
    """Search the project's sheets

     Finds values that contain valueContains, ignoring case, in every indexed column of the project's
    TABLE sheets. Returns a page of hits, one per distinct value in a column of a sheet. Each hit's
    rowCount is the number of rows in that sheet with the value in that column.

    Args:
        project_id (str):
        value_contains (str):
        limit (int | Unset):  Default: 100.
        page (int | Unset):  Default: 1.
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SheetSearchResponse
    """

    try:
        return (
            await asyncio_detailed(
                project_id=project_id,
                client=client,
                value_contains=value_contains,
                limit=limit,
                page=page,
            )
        ).parsed
    except errors.NotFoundException:
        return None
