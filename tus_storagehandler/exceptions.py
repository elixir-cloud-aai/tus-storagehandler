"""Tus Storage Handler exceptions."""

from connexion.exceptions import BadRequestProblem
from werkzeug.exceptions import (
    InternalServerError,
    NotFound,
)

exceptions = {
    Exception: {
        "message": "Oops, something unexpected happened.",
        "code": 500,
    },
    BadRequestProblem: {
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
        "message": "We seem to be having a problem here in the tus storage handler.",
        "code": 500,
    },
}