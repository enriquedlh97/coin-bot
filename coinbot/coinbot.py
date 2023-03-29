"""Slack Coin Bot."""
import random
from typing import Union


class CoinBot:
    """Coin Bot class for defining payload."""

    channel: str
    # Default text for the message
    # TODO: Make COIN_BLOCK a typed dict, custom object
    COIN_BLOCK: dict[str, str | dict[str, str]] = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Sure! Flipping a coin....\n\n",
        },
    }

    def __init__(self, channel: str) -> None:
        """Constructor.

        :param channel: Channel Name.
        """
        self.channel = channel

    def _flip_coin(self) -> dict[str, str | dict[str, str]]:
        """Flip a coin.

        :return: _description_
        """
        rand_int: int = random.randint(0, 1)
        if rand_int == 0:
            results = "Heads"
        else:
            results = "Tails"

        text: str = f"The result is {results}"

        return {"type": "section", "text": {"type": "mrkdwn", "text": text}}

    def get_message_payload(
        self,
    ) -> dict[str, str | list[dict[str, Union[str, dict[str, str]]]]]:
        """_summary_.

        :return:
        """
        return {
            "channel": self.channel,
            "blocks": [
                self.COIN_BLOCK,
                self._flip_coin(),  # type: ignore
            ],
        }
