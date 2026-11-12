from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...models.sheet_diff_request import SheetDiffRequest
from ...models.sheet_diff_response import SheetDiffResponse
from ...types import Response


def _get_kwargs(
    project_id: str,
    sheet_id: str,
    *,
    body: SheetDiffRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/sheets/{sheet_id}/data/diff".format(
            project_id=quote(str(project_id), safe=""),
            sheet_id=quote(str(sheet_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> SheetDiffResponse | None:
    if response.status_code == 200:
        response_200 = SheetDiffResponse.from_dict(response.json())

        return response_200

    errors.handle_error_response(response, client.raise_on_unexpected_status)


def _build_response(*, client: Client, response: httpx.Response) -> Response[SheetDiffResponse]:
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
    body: SheetDiffRequest,
) -> Response[SheetDiffResponse]:
    """Diff sheet snapshots

     Returns paginated rows added, deleted or updated between two snapshots of a TABLE sheet, with each
    row's values as of fromSnapshotId (before) and toSnapshotId (after). Rows are matched by _row_id,
    which an update keeps, so a row deleted and inserted again shows as DELETED and ADDED. A row counts
    as UPDATED when a commit in between rewrote it.

    Args:
        project_id (str):
        sheet_id (str):
        body (SheetDiffRequest): Paginated row changes between two snapshots of a TABLE sheet
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SheetDiffResponse]
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
    body: SheetDiffRequest,
) -> SheetDiffResponse | None:
    """Diff sheet snapshots

     Returns paginated rows added, deleted or updated between two snapshots of a TABLE sheet, with each
    row's values as of fromSnapshotId (before) and toSnapshotId (after). Rows are matched by _row_id,
    which an update keeps, so a row deleted and inserted again shows as DELETED and ADDED. A row counts
    as UPDATED when a commit in between rewrote it.

    Args:
        project_id (str):
        sheet_id (str):
        body (SheetDiffRequest): Paginated row changes between two snapshots of a TABLE sheet
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SheetDiffResponse
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
    body: SheetDiffRequest,
) -> Response[SheetDiffResponse]:
    """Diff sheet snapshots

     Returns paginated rows added, deleted or updated between two snapshots of a TABLE sheet, with each
    row's values as of fromSnapshotId (before) and toSnapshotId (after). Rows are matched by _row_id,
    which an update keeps, so a row deleted and inserted again shows as DELETED and ADDED. A row counts
    as UPDATED when a commit in between rewrote it.

    Args:
        project_id (str):
        sheet_id (str):
        body (SheetDiffRequest): Paginated row changes between two snapshots of a TABLE sheet
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SheetDiffResponse]
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
    body: SheetDiffRequest,
) -> SheetDiffResponse | None:
    """Diff sheet snapshots

     Returns paginated rows added, deleted or updated between two snapshots of a TABLE sheet, with each
    row's values as of fromSnapshotId (before) and toSnapshotId (after). Rows are matched by _row_id,
    which an update keeps, so a row deleted and inserted again shows as DELETED and ADDED. A row counts
    as UPDATED when a commit in between rewrote it.

    Args:
        project_id (str):
        sheet_id (str):
        body (SheetDiffRequest): Paginated row changes between two snapshots of a TABLE sheet
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SheetDiffResponse
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
