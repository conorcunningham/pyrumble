from .connection import Connection


class Organization:
    def __init__(self, connection):
        self.connection: Connection = connection

    def get_assets(self, **kwargs) -> list[dict]:
        """
        Get assets
        :param kwargs: Kwargs to pass to the request params for URL query params
        :return: A list of assets
        """
        url = "org/assets"
        return self.connection.get(url, params=kwargs)

    def retrieve_asset(self, asset_id):
        url = f"org/assets/{asset_id}"
        return self.connection.get(url)

    def delete_assets(self, asset_id):
        """
        Delete a single asset
        :param asset_id: The ID of the asset to be deleted
        :return:
        """
        url = f"org/assets/{asset_id}"
        return self.connection.delete(url)

    def update_asset_comments(self, asset_id, data):
        url = f"org/assets/{asset_id}/comments"
        return self.connection.patch(url, data)

    def update_asset_tags(self, asset_id, data):
        url = f"org/assets/{asset_id}/tags"
        return self.connection.patch(url, data)

    def get_agents(self):
        url = f"org/assets"
        return self.connection.get(url)

    def retrieve_agent(self, agent_id):
        url = f"org/assets/{agent_id}"
        return self.connection.get(url)
