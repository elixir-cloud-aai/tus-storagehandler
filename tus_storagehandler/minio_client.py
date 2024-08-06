"""Minio Client Configuration Module.

This module initializes a Minio client using environment variables
loaded via dotenv. It also provides a function to create a new Minio
bucket if it does not already exist.
"""

from tus_storage_handler.consts import (
  MINIO_ACCESS_KEY,
  MINIO_BUCKET,
  MINIO_ENDPOINT,
  MINIO_IS_SECURE,
  MINIO_SECRET_KEY,
)
from minio import Minio

minio_client = Minio(
  endpoint=MINIO_ENDPOINT,
  access_key=MINIO_ACCESS_KEY,
  secret_key=MINIO_SECRET_KEY,
  secure=MINIO_IS_SECURE,
)


def create_bucket():
  """Creates a new bucket if it does not already exist.

  This function checks if the bucket specified by MINIO_BUCKET exists.
  If it does not exist, it creates a new bucket using the Minio client instance.
  """
  if not minio_client.bucket_exists(MINIO_BUCKET):
    minio_client.make_bucket(MINIO_BUCKET)


create_bucket()