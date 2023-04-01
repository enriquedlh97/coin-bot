"""Coin bot testing."""
from typing import Union

from configs import config
from slack import WebClient

from coinbot import CoinBot

# Create a slack client
slack_web_client: WebClient = WebClient(token=config.SLACK_TOKEN)

# Get a new CoinBot
coin_bot: CoinBot = CoinBot(config.APP_CONFIG.COINBOT_CHANNEL)  # Channel name

# Get the onboarding message payload
message: dict[
    str, str | list[dict[str, Union[str, dict[str, str]]]]
] = coin_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)  # type: ignore
