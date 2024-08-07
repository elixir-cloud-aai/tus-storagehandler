"""Tus Storage Handler exceptions."""

from werkzeug.exceptions import BadRequest, InternalServerError, NotFound


class GenericException(Exception):
    """A generic exception for the Tus Storage Handler."""

    pass


exceptions = {
    Exception: {
        "message": "Oops, something unexpected happened.",
        "code": 500,
    },
    BadRequest: {
        "message": "We don't quite understand what it is you are looking for.",
        "code": 400,
    },
    NotFound: {
        "message": "We do not have this file in our storage",
        "code": 404,
    },
    InternalServerError: {
        "message": "An internal server error occurred in the tus storage handler",
        "code": 500,
    },
    GenericException: {
        "message": "An unexpected error occurred",
        "code": 500,
    },
}
