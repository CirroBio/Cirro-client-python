from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...models.sheet_search_request import SheetSearchRequest
from ...models.sheet_search_response import SheetSearchResponse
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: SheetSearchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/sheets/search".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: SheetSearchRequest,
) -> Response[SheetSearchResponse]:
    """Search the project's sheets

     Finds values that contain valueContains, ignoring case, in every indexed column of the project's
    TABLE sheets. Returns a page of hits, one per distinct value in a column of a sheet. Each hit's
    rowCount is the number of rows in that sheet with the value in that column.

    Args:
        project_id (str):
        body (SheetSearchRequest): Search across the indexed columns of the project's TABLE sheets
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SheetSearchResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
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
    body: SheetSearchRequest,
) -> SheetSearchResponse | None:
    """Search the project's sheets

     Finds values that contain valueContains, ignoring case, in every indexed column of the project's
    TABLE sheets. Returns a page of hits, one per distinct value in a column of a sheet. Each hit's
    rowCount is the number of rows in that sheet with the value in that column.

    Args:
        project_id (str):
        body (SheetSearchRequest): Search across the indexed columns of the project's TABLE sheets
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
            body=body,
        ).parsed
    except errors.NotFoundException:
        return None


async def asyncio_detailed(
    project_id: str,
    *,
    client: Client,
    body: SheetSearchRequest,
) -> Response[SheetSearchResponse]:
    """Search the project's sheets

     Finds values that contain valueContains, ignoring case, in every indexed column of the project's
    TABLE sheets. Returns a page of hits, one per distinct value in a column of a sheet. Each hit's
    rowCount is the number of rows in that sheet with the value in that column.

    Args:
        project_id (str):
        body (SheetSearchRequest): Search across the indexed columns of the project's TABLE sheets
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SheetSearchResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: Client,
    body: SheetSearchRequest,
) -> SheetSearchResponse | None:
    """Search the project's sheets

     Finds values that contain valueContains, ignoring case, in every indexed column of the project's
    TABLE sheets. Returns a page of hits, one per distinct value in a column of a sheet. Each hit's
    rowCount is the number of rows in that sheet with the value in that column.

    Args:
        project_id (str):
        body (SheetSearchRequest): Search across the indexed columns of the project's TABLE sheets
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
                body=body,
            )
        ).parsed
    except errors.NotFoundException:
        return None
