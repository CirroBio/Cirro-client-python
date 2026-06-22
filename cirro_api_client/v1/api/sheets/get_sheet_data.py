from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...models.sheet_query_response import SheetQueryResponse
from ...models.sql_sort_order import SqlSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    sheet_id: str,
    *,
    limit: int | Unset = 1000,
    page: int | Unset = 1,
    order_by: None | str | Unset = UNSET,
    order: SqlSortOrder | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["page"] = page

    json_order_by: None | str | Unset
    if isinstance(order_by, Unset):
        json_order_by = UNSET
    else:
        json_order_by = order_by
    params["orderBy"] = json_order_by

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/sheets/{sheet_id}/data".format(
            project_id=quote(str(project_id), safe=""),
            sheet_id=quote(str(sheet_id), safe=""),
        ),
        "params": params,
    }

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
    limit: int | Unset = 1000,
    page: int | Unset = 1,
    order_by: None | str | Unset = UNSET,
    order: SqlSortOrder | Unset = UNSET,
) -> Response[SheetQueryResponse]:
    """Get sheet data

     Returns paginated rows from a sheet. The first column is always _row_id, which uniquely identifies
    each row and is required for row updates via PUT. Defaults page=1, limit=1000, order=ASCENDING.

    Args:
        project_id (str):
        sheet_id (str):
        limit (int | Unset):  Default: 1000.
        page (int | Unset):  Default: 1.
        order_by (None | str | Unset):
        order (SqlSortOrder | Unset):
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
        limit=limit,
        page=page,
        order_by=order_by,
        order=order,
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
    limit: int | Unset = 1000,
    page: int | Unset = 1,
    order_by: None | str | Unset = UNSET,
    order: SqlSortOrder | Unset = UNSET,
) -> SheetQueryResponse | None:
    """Get sheet data

     Returns paginated rows from a sheet. The first column is always _row_id, which uniquely identifies
    each row and is required for row updates via PUT. Defaults page=1, limit=1000, order=ASCENDING.

    Args:
        project_id (str):
        sheet_id (str):
        limit (int | Unset):  Default: 1000.
        page (int | Unset):  Default: 1.
        order_by (None | str | Unset):
        order (SqlSortOrder | Unset):
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
            limit=limit,
            page=page,
            order_by=order_by,
            order=order,
        ).parsed
    except errors.NotFoundException:
        return None


async def asyncio_detailed(
    project_id: str,
    sheet_id: str,
    *,
    client: Client,
    limit: int | Unset = 1000,
    page: int | Unset = 1,
    order_by: None | str | Unset = UNSET,
    order: SqlSortOrder | Unset = UNSET,
) -> Response[SheetQueryResponse]:
    """Get sheet data

     Returns paginated rows from a sheet. The first column is always _row_id, which uniquely identifies
    each row and is required for row updates via PUT. Defaults page=1, limit=1000, order=ASCENDING.

    Args:
        project_id (str):
        sheet_id (str):
        limit (int | Unset):  Default: 1000.
        page (int | Unset):  Default: 1.
        order_by (None | str | Unset):
        order (SqlSortOrder | Unset):
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
        limit=limit,
        page=page,
        order_by=order_by,
        order=order,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    sheet_id: str,
    *,
    client: Client,
    limit: int | Unset = 1000,
    page: int | Unset = 1,
    order_by: None | str | Unset = UNSET,
    order: SqlSortOrder | Unset = UNSET,
) -> SheetQueryResponse | None:
    """Get sheet data

     Returns paginated rows from a sheet. The first column is always _row_id, which uniquely identifies
    each row and is required for row updates via PUT. Defaults page=1, limit=1000, order=ASCENDING.

    Args:
        project_id (str):
        sheet_id (str):
        limit (int | Unset):  Default: 1000.
        page (int | Unset):  Default: 1.
        order_by (None | str | Unset):
        order (SqlSortOrder | Unset):
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
                limit=limit,
                page=page,
                order_by=order_by,
                order=order,
            )
        ).parsed
    except errors.NotFoundException:
        return None
