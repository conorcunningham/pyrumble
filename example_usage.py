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
