# Cirro API Client
[![](https://img.shields.io/pypi/v/cirro-api-client.svg)](https://pypi.org/project/cirro_api_client/)

Low-level client for the Cirro API. Rather than using this package directly, we recommend using the [Cirro SDK](https://github.com/CirroBio/Cirro-client).

This Python package is automatically generated by the [OpenAPI Python Client](https://github.com/openapi-generators/openapi-python-client) project.

## Requirements.

Python 3.8+.

## Installation & Usage
### pip install

Via PyPI:
```sh
pip install cirro-api-client
```

You can also install it directory from the repository using:

```sh
pip install git+https://github.com/CirroBio/Cirro-client-python.git
```

## Getting Started

### Basic usage

```python
import os
from typing import List
from pprint import pprint

from cirro_api_client import CirroApiClient, TokenAuth
from cirro_api_client.v1.api.projects import get_projects
from cirro_api_client.v1.models import Project
from cirro_api_client.v1.types import Response

# Create auth method, you can also extend the AuthMethod class
auth_method = TokenAuth(token=os.environ['TOKEN'])
# You can also use the RefreshableTokenAuth class
# auth_method = RefreshableTokenAuth(token_getter=lambda : os.environ['TOKEN'])

# Create a client
client = CirroApiClient(base_url="https://api.cirro.bio",
                        auth_method=auth_method)

# Call API endpoint, get list of projects
projects: List[Project] = get_projects.sync(client=client)
print("The response of get_projects:\n")
pprint(projects)
## or if you need more info (e.g. status_code)
resp: Response[List[Project]] = get_projects.sync_detailed(client=client)
projects = resp.parsed
```

### Async usage
```python
import os
from typing import List

from cirro_api_client import CirroApiClient, TokenAuth
from cirro_api_client.v1.api.projects import get_projects
from cirro_api_client.v1.models import Project

client = CirroApiClient(base_url="https://api.cirro.bio",
                        auth_method=TokenAuth(token=os.environ['TOKEN']))

# async method
async with client as client:
    projects: List[Project] = await get_projects.asyncio(client=client)
```

### Advanced usage

There are more settings on the generated `CirroApiClient` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.Client` or `httpx.AsyncClient` (depending on your use-case):

```python
import os
from cirro_api_client import CirroApiClient, TokenAuth

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = CirroApiClient(
    base_url="https://api.cirro.bio",
    auth_method=TokenAuth(token=os.environ['TOKEN']),
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

You can even set the httpx client directly, but beware that this will override any existing settings (e.g., base_url):

```python
import os
import httpx
from cirro_api_client import CirroApiClient, TokenAuth

client = CirroApiClient(base_url="https://api.cirro.bio",
                        auth_method=TokenAuth(token=os.environ['TOKEN']))

# Note that base_url needs to be re-set, as would any shared cookies, headers, etc.
client.set_httpx_client(httpx.Client(base_url="https://api.cirro.bio", proxies="http://localhost:8030"))
```

## Developer information

Re-generate the API client by running:

```sh
openapi-python-client update --url https://dev.cirro.bio/openapi/cirro-data-latest.yml --config config.yml --custom-template-path=templates/
 ```
