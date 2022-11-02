from enum import Enum


class GlobalErrorMessages(Enum):
    """Global constance errors messages."""

    WRONG_STATUS_CODE = "Received status code is not expected."
    WRONG_ELEMENTS_COUNT = "Number of elements is not equal to expected."
