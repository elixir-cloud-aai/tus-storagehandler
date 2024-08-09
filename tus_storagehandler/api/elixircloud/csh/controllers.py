"""Cloud Storage Handler controllers."""

import logging

from exceptions import NotFound

logger = logging.getLogger(__name__)

from flask import jsonify, request


def home():
    """Endpoint to return a welcome message."""
    return jsonify({"message": "Welcome to the Cloud Storage Handler server!"}), 200
