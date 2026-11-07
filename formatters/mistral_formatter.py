from agentscope.formatter import OpenAIChatFormatter
from agentscope.message import Msg


class MistralFormatter(OpenAIChatFormatter):

    async def format(self, msgs: list[Msg]) -> list[dict]:
        messages = await super().format(msgs)

        for message in messages:
            if message["role"] != "tool":
                message.pop("name", None)

        return messages