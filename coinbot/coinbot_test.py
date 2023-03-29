"""Coin bot testing."""
import os
from typing import Union

from slack import WebClient

from coinbot import CoinBot

# Create a slack client
slack_web_client: WebClient = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Get a new CoinBot
coin_bot: CoinBot = CoinBot("#bot-dev")  # Channel name

# Get the onboarding message payload
message: dict[
    str,
    str
    | list[
        dict[str, Union[str, dict[str, str | tuple[str]]]],
    ],
] = coin_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)
