# Rumble Run API Client

### A simple Python client for working with the Rumble Run API

**Very much in beta beta beta**

Pyrumble is a simple API client for the [Rumble Run](https://rumble.run) API. It currently only supports operations for the `organisation/assets` endpoint, but more will be coming soon.

Please feel free to contribute if you wish, it will be much appreciated

## Usage

All you need to get started is your API Key and the Rumble API URL. Here's an example of how the client can be used.

```python
import os
from pyrumble.client import Rumble


base_url = "https://console.rumble.run/api/v1.0/"
api_key = os.getenv("API_KEY", None)

if api_key is None:
    raise Exception("A valid API key must be set as an environmental variable, API_KEY")

# instantiate rumble and get some assets
rumble = Rumble(base_url, api_key)
devices = rumble.organization.get_assets()

# retrieve a single asset
my_device = rumble.organization.retrieve_asset(devices[0]['id'])

# adds some query filters
query_params = {"type": "switch", "site": "my site", "os": "Cisco IOS 12"}
filtered_devices = rumble.organization.get_assets(**query_params)

# print out all names for all devices
for device in filtered_devices:
    print([device['names']])

```


