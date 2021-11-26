from .exceptions import ClientException
from .organization import Organization
from .connection import Connection


class Rumble:
    """
    Base class for all things Rumble client
    """

    def __init__(
        self,
        base_url: str,
        api_key: str,
    ):
        if base_url is None or api_key is None:
            raise ClientException("Host and API Key must not be have a valid value")

        self.base_url = base_url
        self.connection = Connection(self.base_url, api_key)
        self.organization = Organization(self.connection)
