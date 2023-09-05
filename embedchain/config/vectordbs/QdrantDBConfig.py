from typing import List, Union

from embedchain.config.BaseConfig import BaseConfig
from embedchain.helper_classes.json_serializable import register_deserializable


@register_deserializable
class QdrantDBConfig(BaseConfig):
    """
    Config to initialize an qdrant client.
    :param url. qdrant url or list of nodes url to be used for connection
    """

    def __init__(self, url: Union[str, List[str]] = None):
        self.URL = url