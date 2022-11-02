import requests

from configuration import SERVICE_URL

from src.base_classes.response import Response
from src.schems.post import POST_SCHEMA


def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
    response = Response(response)

    response.assert_status_code(200)
    response.validate(POST_SCHEMA)
