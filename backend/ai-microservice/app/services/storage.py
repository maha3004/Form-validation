from typing import Iterable

import boto3
from botocore.exceptions import BotoCoreError, ClientError
from loguru import logger

from ..config import get_settings


class StorageService:
    def __init__(self):
        settings = get_settings()
        self.s3 = boto3.client("s3", region_name=settings.aws_region)
        self.bucket = settings.s3_bucket

    def upload_text(self, key: str, text: str) -> None:
        try:
            self.s3.put_object(Bucket=self.bucket, Key=key, Body=text.encode("utf-8"))
            logger.info("Uploaded summary to S3 at {}", key)
        except (BotoCoreError, ClientError) as exc:
            logger.error("Failed to upload to S3: {}", exc)
            raise

    def download_text(self, key: str) -> str:
        try:
            response = self.s3.get_object(Bucket=self.bucket, Key=key)
            return response["Body"].read().decode("utf-8")
        except (BotoCoreError, ClientError) as exc:
            logger.error("Failed to download from S3: {}", exc)
            raise

    def list_keys(self, prefix: str = "") -> Iterable[str]:
        paginator = self.s3.get_paginator("list_objects_v2")
        for page in paginator.paginate(Bucket=self.bucket, Prefix=prefix):
            for obj in page.get("Contents", []):
                yield obj["Key"]
