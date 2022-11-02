import requests

from configuration import SERVICE_URL

from src.base_classes.response import Response
# from src.scheme.post import POST_SCHEME
from src.pydantic_scheme.post import Post


def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
    response = Response(response)

    response.assert_status_code(200).validate(Post)
