"""Tus Storage Handler exceptions."""

from werkzeug.exceptions import BadRequest, InternalServerError, NotFound

exceptions = {
    Exception: {
        "message": "An unexpected error occurred. Please try again.",
        "code": 500,
    },
    BadRequest: {
        "message": "Invalid request. Please check your input and try again.",
        "code": 400,
    },
    NotFound: {
        "message": "The requested resource could not be found.",
        "code": 404,
    },
    InternalServerError: {
        "message": "An internal server error occurred in the tus storage handler",
        "code": 500,
    },
}
