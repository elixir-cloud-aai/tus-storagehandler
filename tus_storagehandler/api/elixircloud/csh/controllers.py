"""Cloud Storage Handler controllers."""

import logging

from flask import jsonify

logger = logging.getLogger(__name__)


def home():
    """Endpoint to return a welcome message."""
    return jsonify({"message": "Welcome to the Cloud Storage Handler server!"}), 200
