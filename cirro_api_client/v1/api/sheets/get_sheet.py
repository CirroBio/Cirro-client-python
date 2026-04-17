from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...models.sheet_detail import SheetDetail
from ...types import Response


def _get_kwargs(
    project_id: str,
    sheet_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/sheets/{sheet_id}".format(
            project_id=quote(str(project_id), safe=""),
            sheet_id=quote(str(sheet_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> SheetDetail | None:
    if response.status_code == 200:
        response_200 = SheetDetail.from_dict(response.json())

        return response_200

    errors.handle_error_response(response, client.raise_on_unexpected_status)


def _build_response(*, client: Client, response: httpx.Response) -> Response[SheetDetail]:
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
) -> Response[SheetDetail]:
    """Get sheet

     Retrieves a sheet

    Args:
        project_id (str):
        sheet_id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SheetDetail]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        sheet_id=sheet_id,
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
) -> SheetDetail | None:
    """Get sheet

     Retrieves a sheet

    Args:
        project_id (str):
        sheet_id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SheetDetail
    """

    try:
        return sync_detailed(
            project_id=project_id,
            sheet_id=sheet_id,
            client=client,
        ).parsed
    except errors.NotFoundException:
        return None


async def asyncio_detailed(
    project_id: str,
    sheet_id: str,
    *,
    client: Client,
) -> Response[SheetDetail]:
    """Get sheet

     Retrieves a sheet

    Args:
        project_id (str):
        sheet_id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SheetDetail]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        sheet_id=sheet_id,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    sheet_id: str,
    *,
    client: Client,
) -> SheetDetail | None:
    """Get sheet

     Retrieves a sheet

    Args:
        project_id (str):
        sheet_id (str):
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SheetDetail
    """

    try:
        return (
            await asyncio_detailed(
                project_id=project_id,
                sheet_id=sheet_id,
                client=client,
            )
        ).parsed
    except errors.NotFoundException:
        return None
