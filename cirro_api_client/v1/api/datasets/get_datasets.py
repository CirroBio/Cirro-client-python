from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_response_dataset_list_dto import PaginatedResponseDatasetListDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    limit: Union[Unset, int] = 10000,
    next_token: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["nextToken"] = next_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/datasets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedResponseDatasetListDto]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedResponseDatasetListDto.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedResponseDatasetListDto]:
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
    limit: Union[Unset, int] = 10000,
    next_token: Union[Unset, str] = UNSET,
) -> Response[PaginatedResponseDatasetListDto]:
    """List datasets

     Retrieves a list of datasets for a given project

    Args:
        project_id (str):
        limit (Union[Unset, int]):  Default: 10000.
        next_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseDatasetListDto]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        limit=limit,
        next_token=next_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: Client,
    limit: Union[Unset, int] = 10000,
    next_token: Union[Unset, str] = UNSET,
) -> Optional[PaginatedResponseDatasetListDto]:
    """List datasets

     Retrieves a list of datasets for a given project

    Args:
        project_id (str):
        limit (Union[Unset, int]):  Default: 10000.
        next_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseDatasetListDto
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        limit=limit,
        next_token=next_token,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: Client,
    limit: Union[Unset, int] = 10000,
    next_token: Union[Unset, str] = UNSET,
) -> Response[PaginatedResponseDatasetListDto]:
    """List datasets

     Retrieves a list of datasets for a given project

    Args:
        project_id (str):
        limit (Union[Unset, int]):  Default: 10000.
        next_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponseDatasetListDto]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        limit=limit,
        next_token=next_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: Client,
    limit: Union[Unset, int] = 10000,
    next_token: Union[Unset, str] = UNSET,
) -> Optional[PaginatedResponseDatasetListDto]:
    """List datasets

     Retrieves a list of datasets for a given project

    Args:
        project_id (str):
        limit (Union[Unset, int]):  Default: 10000.
        next_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponseDatasetListDto
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            limit=limit,
            next_token=next_token,
        )
    ).parsed
