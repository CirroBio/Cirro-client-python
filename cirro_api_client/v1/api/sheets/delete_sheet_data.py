from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...models.delete_rows_request import DeleteRowsRequest
from ...models.sheet_data_update_response import SheetDataUpdateResponse
from ...types import Response


def _get_kwargs(
    project_id: str,
    sheet_id: str,
    *,
    body: DeleteRowsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/projects/{project_id}/sheets/{sheet_id}/data".format(
            project_id=quote(str(project_id), safe=""),
            sheet_id=quote(str(sheet_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> SheetDataUpdateResponse | None:
    if response.status_code == 200:
        response_200 = SheetDataUpdateResponse.from_dict(response.json())

        return response_200

    errors.handle_error_response(response, client.raise_on_unexpected_status)


def _build_response(*, client: Client, response: httpx.Response) -> Response[SheetDataUpdateResponse]:
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
    body: DeleteRowsRequest,
) -> Response[SheetDataUpdateResponse]:
    """Delete sheet rows

     Returns number of rows deleted. Deletes specific rows from a sheet by _row_id. The request body
    lists the rowIds to delete.

    Args:
        project_id (str):
        sheet_id (str):
        body (DeleteRowsRequest):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SheetDataUpdateResponse]
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
    body: DeleteRowsRequest,
) -> SheetDataUpdateResponse | None:
    """Delete sheet rows

     Returns number of rows deleted. Deletes specific rows from a sheet by _row_id. The request body
    lists the rowIds to delete.

    Args:
        project_id (str):
        sheet_id (str):
        body (DeleteRowsRequest):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SheetDataUpdateResponse
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
    body: DeleteRowsRequest,
) -> Response[SheetDataUpdateResponse]:
    """Delete sheet rows

     Returns number of rows deleted. Deletes specific rows from a sheet by _row_id. The request body
    lists the rowIds to delete.

    Args:
        project_id (str):
        sheet_id (str):
        body (DeleteRowsRequest):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SheetDataUpdateResponse]
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
    body: DeleteRowsRequest,
) -> SheetDataUpdateResponse | None:
    """Delete sheet rows

     Returns number of rows deleted. Deletes specific rows from a sheet by _row_id. The request body
    lists the rowIds to delete.

    Args:
        project_id (str):
        sheet_id (str):
        body (DeleteRowsRequest):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SheetDataUpdateResponse
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
