from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...models.sheet_data_request import SheetDataRequest
from ...models.sheet_query_response import SheetQueryResponse
from ...types import Response


def _get_kwargs(
    project_id: str,
    sheet_id: str,
    *,
    body: SheetDataRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/sheets/{sheet_id}/data/query".format(
            project_id=quote(str(project_id), safe=""),
            sheet_id=quote(str(sheet_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> SheetQueryResponse | None:
    if response.status_code == 200:
        response_200 = SheetQueryResponse.from_dict(response.json())

        return response_200

    errors.handle_error_response(response, client.raise_on_unexpected_status)


def _build_response(*, client: Client, response: httpx.Response) -> Response[SheetQueryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    sheet_id: str,
    *,
    client: Client,
    body: SheetDataRequest,
) -> Response[SheetQueryResponse]:
    """Query sheet data

     Returns paginated rows from a sheet. The first column is always _row_id, which uniquely identifies
    each row and is required for row updates via PUT. This is essentially a GET request disguised as a
    POST so we can pass in a body.

    Args:
        project_id (str):
        sheet_id (str):
        body (SheetDataRequest): Paginated sheet data query with optional sort and filter
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SheetQueryResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        sheet_id=sheet_id,
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
    *,
    client: Client,
    body: SheetDataRequest,
) -> SheetQueryResponse | None:
    """Query sheet data

     Returns paginated rows from a sheet. The first column is always _row_id, which uniquely identifies
    each row and is required for row updates via PUT. This is essentially a GET request disguised as a
    POST so we can pass in a body.

    Args:
        project_id (str):
        sheet_id (str):
        body (SheetDataRequest): Paginated sheet data query with optional sort and filter
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SheetQueryResponse
    """

    try:
        return sync_detailed(
            project_id=project_id,
            sheet_id=sheet_id,
            client=client,
            body=body,
        ).parsed
    except errors.NotFoundException:
        return None


async def asyncio_detailed(
    project_id: str,
    sheet_id: str,
    *,
    client: Client,
    body: SheetDataRequest,
) -> Response[SheetQueryResponse]:
    """Query sheet data

     Returns paginated rows from a sheet. The first column is always _row_id, which uniquely identifies
    each row and is required for row updates via PUT. This is essentially a GET request disguised as a
    POST so we can pass in a body.

    Args:
        project_id (str):
        sheet_id (str):
        body (SheetDataRequest): Paginated sheet data query with optional sort and filter
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SheetQueryResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        sheet_id=sheet_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    sheet_id: str,
    *,
    client: Client,
    body: SheetDataRequest,
) -> SheetQueryResponse | None:
    """Query sheet data

     Returns paginated rows from a sheet. The first column is always _row_id, which uniquely identifies
    each row and is required for row updates via PUT. This is essentially a GET request disguised as a
    POST so we can pass in a body.

    Args:
        project_id (str):
        sheet_id (str):
        body (SheetDataRequest): Paginated sheet data query with optional sort and filter
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SheetQueryResponse
    """

    try:
        return (
            await asyncio_detailed(
                project_id=project_id,
                sheet_id=sheet_id,
                client=client,
                body=body,
            )
        ).parsed
    except errors.NotFoundException:
        return None
