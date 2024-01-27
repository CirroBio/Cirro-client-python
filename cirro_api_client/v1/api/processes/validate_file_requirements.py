from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_requirements import FileRequirements
from ...models.validate_file_requirements_request import ValidateFileRequirementsRequest
from ...types import Response


def _get_kwargs(
    process_id: str,
    *,
    body: ValidateFileRequirementsRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/processes/{process_id}/validate-files",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[FileRequirements]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FileRequirements.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FileRequirements]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    process_id: str,
    *,
    client: AuthenticatedClient,
    body: ValidateFileRequirementsRequest,
) -> Response[FileRequirements]:
    """Validate file requirements

     Checks the input file names with the expected files for a data type (ingest processes only)

    Args:
        process_id (str):
        body (ValidateFileRequirementsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileRequirements]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    process_id: str,
    *,
    client: AuthenticatedClient,
    body: ValidateFileRequirementsRequest,
) -> Optional[FileRequirements]:
    """Validate file requirements

     Checks the input file names with the expected files for a data type (ingest processes only)

    Args:
        process_id (str):
        body (ValidateFileRequirementsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileRequirements
    """

    return sync_detailed(
        process_id=process_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    process_id: str,
    *,
    client: AuthenticatedClient,
    body: ValidateFileRequirementsRequest,
) -> Response[FileRequirements]:
    """Validate file requirements

     Checks the input file names with the expected files for a data type (ingest processes only)

    Args:
        process_id (str):
        body (ValidateFileRequirementsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileRequirements]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    process_id: str,
    *,
    client: AuthenticatedClient,
    body: ValidateFileRequirementsRequest,
) -> Optional[FileRequirements]:
    """Validate file requirements

     Checks the input file names with the expected files for a data type (ingest processes only)

    Args:
        process_id (str):
        body (ValidateFileRequirementsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileRequirements
    """

    return (
        await asyncio_detailed(
            process_id=process_id,
            client=client,
            body=body,
        )
    ).parsed
