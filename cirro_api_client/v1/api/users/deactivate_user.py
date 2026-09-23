from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    username: str,
    *,
    remove_from_projects: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["removeFromProjects"] = remove_from_projects

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/users/{username}:deactivate".format(
            username=quote(str(username), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    errors.handle_error_response(response, client.raise_on_unexpected_status)


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: Client,
    remove_from_projects: bool | Unset = False,
) -> Response[Any]:
    """Deactivate user

     Deactivates a user, blocking sign in and revoking their tokens

    Args:
        username (str):
        remove_from_projects (bool | Unset):  Default: False.
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        username=username,
        remove_from_projects=remove_from_projects,
    )

    response = client.get_httpx_client().request(
        auth=client.get_auth(),
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    username: str,
    *,
    client: Client,
    remove_from_projects: bool | Unset = False,
) -> Response[Any]:
    """Deactivate user

     Deactivates a user, blocking sign in and revoking their tokens

    Args:
        username (str):
        remove_from_projects (bool | Unset):  Default: False.
        client (Client): instance of the API client

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        username=username,
        remove_from_projects=remove_from_projects,
    )

    response = await client.get_async_httpx_client().request(auth=client.get_auth(), **kwargs)

    return _build_response(client=client, response=response)
