import json
from typing import Dict

import boto3
from botocore.exceptions import BotoCoreError, ClientError
from loguru import logger

from ..config import get_settings


class NotificationService:
    def __init__(self):
        settings = get_settings()
        self.sns = boto3.client("sns", region_name=settings.aws_region)
        self.topic_next_day = settings.sns_topic_next_day
        self.topic_post_class = settings.sns_topic_post_class

    def publish_next_day(self, message: Dict):
        self._publish(self.topic_next_day, message)

    def publish_post_class(self, message: Dict):
        self._publish(self.topic_post_class, message)

    def _publish(self, topic_arn: str, message: Dict):
        try:
            self.sns.publish(TopicArn=topic_arn, Message=json.dumps(message))
            logger.info("Published notification to {}", topic_arn)
        except (BotoCoreError, ClientError) as exc:
            logger.error("Failed to publish notification: {}", exc)
            raise
